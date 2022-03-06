FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DB_NAME=notes
ENV DB_PASSWORD=postgres
ENV DB_USER=postgres
ENV DB_PORT=5432
ENV DB_HOST=db

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/