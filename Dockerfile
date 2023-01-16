FROM python:3.9-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/worker
COPY . .
RUN pip install -r $APP_PATH/requirements.txt

CMD ["python3", "-m", "$APP_PATH/app.py"]