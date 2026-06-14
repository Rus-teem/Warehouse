# Dockerfile для Python-приложения (аналитика)
# Использует официальный образ Python 3.11 slim

FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD ["python", "app.py"]
