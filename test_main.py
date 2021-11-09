from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome": "Movie Recommendation API Home"}


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": 200, "is_model_loaded": True}


def test_predict():
    response = client.post(
        "/predict",
        json={"user_id": 0, "nrec_items": 10},
    )
    assert response.status_code == 200
    assert response.json() == {
        "prediction": [
            "Return of the Jedi (1983)",
            "Star Wars (1977)",
            "Pulp Fiction (1994)",
            "Fargo (1996)",
            "Raiders of the Lost Ark (1981)",
            "Empire Strikes Back, The (1980)",
            "Monty Python and the Holy Grail (1974)",
            "Back to the Future (1985)",
            "Independence Day (ID4) (1996)",
            "Silence of the Lambs, The (1991)",
        ]
    }


def test_predict_nonexistent_user():
    response = client.post(
        "/predict",
        json={"user_id": 99999999, "nrec_items": 10},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found."}


def test_predict_missing_value():
    response = client.post(
        "/predict",
        json={"user_id": 0},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "nrec_items"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
