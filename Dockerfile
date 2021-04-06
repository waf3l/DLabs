FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install wheel
RUN pip install -r requirements.txt