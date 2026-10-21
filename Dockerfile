FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY  app .
EXPOSE 5000
ENV  FLASK_APP=app:create_app
CMD ["flask" , "run" , "--host=0.0.0.0" , "--port=5000"]
