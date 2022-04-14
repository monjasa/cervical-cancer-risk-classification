FROM tiangolo/uvicorn-gunicorn:python3.9-slim

COPY ./requirements.txt /app/requirements.txt
COPY ./models /models

RUN pip install -r /app/requirements.txt && rm -rf /root/.cache
COPY ./app /app
