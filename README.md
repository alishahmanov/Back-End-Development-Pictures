# Back-End-Development-Pictures

Flask API for the Djirection concert gallery. The service loads its sample records from `backend/data/pictures.json`.

Install the dependencies and run the service with `python -m flask --app app run --port 5000`. Run the starter tests with `python -m pytest -v`.

The API supports `GET /health`, `GET /count`, `GET /picture`, `POST /picture`, and GET, PUT, and DELETE on `/picture/<id>`.

## Environment Setup

In IBM Skills Network Cloud IDE, clone this repository, open the terminal in its root, and initialize the environment:

```sh
git clone https://github.com/alishahmanov/Back-End-Development-Pictures.git
cd Back-End-Development-Pictures
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask pytest
python -m pytest -v
python -m flask --app app run --port 5000
```

In a second terminal, verify `curl -i http://127.0.0.1:5000/health` and `curl -i http://127.0.0.1:5000/count`. The supplied suite covers health, count, retrieval, creation, update, and deletion.
