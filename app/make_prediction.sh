curl -d '{"user_id": 0, "nrec_items": 10}' \
     -H "Content-Type: application/json" \
     -X POST http://localhost:$1/predict
