# Back-End-Development-Pictures

Flask API for the Djirection concert gallery. The service loads its sample records from `backend/data/pictures.json`.

Install the dependencies and run the service with `python -m flask --app app run --port 5000`. Run the starter tests with `python -m pytest -v`.

The API supports `GET /health`, `GET /count`, `GET /picture`, `POST /picture`, and GET, PUT, and DELETE on `/picture/<id>`.
