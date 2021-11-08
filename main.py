from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import pickle5 as pickle
import numpy as np


description = """
Recommend movie based on **user_id** and **nrec_items**:
- **user_id**: user id
- **nrec_items**: the number of items returned
"""
app = FastAPI(
    title="Movie Personalization API",
    description=description,
    version="1.0.0",
)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger()

is_model_loaded = False
model = None


def load_model(is_forced=False):
    global model
    global item_features
    global item_map
    global is_model_loaded

    if is_forced or not model:
        logger.info("loading model....")
        try:
            with open("model/model.pickle", "rb") as handle:
                model = pickle.load(handle)
            with open("model/item_features.pickle", "rb") as handle:
                item_features = pickle.load(handle)
            with open("model/item_map.pickle", "rb") as handle:
                item_map = pickle.load(handle)

            is_model_loaded = True
            logger.info("model is succesfully loaded into memory")
        except Exception as e:
            is_model_loaded = False
            logger.error(f"model failed to be loaded into memory: {e}")
        return is_model_loaded

    logger.info("model had already been loaded into memory")
    return is_model_loaded


load_model(True)


class Features(BaseModel):
    user_id: int
    nrec_items: int

    class Config:
        schema_extra = {
            "example": {
                "user_id": 0,
                "nrec_items": 10,
            }
        }


@app.get("/")
def home():
    return {"Welcome": "Movie Recommendation API Home"}


@app.get("/healthcheck")
def healthcheck():
    response = {
        "status": 200,
        "is_model_loaded": is_model_loaded,
    }
    logger.debug(f"healthcheck response: {response}")
    return response


@app.post("/predict")
async def predict(features: Features):
    global model
    global item_features
    global item_map

    logger.info(f"features: {features}")

    if (features.user_id) > 942 or (features.user_id) < 0:
        raise HTTPException(status_code=404, detail="User not found.")

    arr = model.predict(features.user_id, np.arange(1682), item_features=item_features)
    sorted_ind = np.argsort(arr)[::-1][: features.nrec_items]
    top_n_items = [item_map[x] for x in sorted_ind]
    logger.info(f"recommendation: {top_n_items}")
    return {"prediction": top_n_items}
