FROM python:3.10-slim-buster
RUN apt-get update
WORKDIR /app
COPY requirements.txt /app/
COPY . /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
EXPOSE 5000