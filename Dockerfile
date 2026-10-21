FROM python:3.16-rc-alpine3.23
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY  app .
EXPOSE 5000
ENV  FLASK_APP=app

