# Используем базовый образ Python 3.8
FROM python:3.9
ENV PYTHONUNBUFFERED=1

# системные зависимости
RUN apt-get update && apt-get install -y \
    python3-distutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install django==3.2
RUN pip install telebot
RUN pip install langchain-gigachat

RUN python manage.py migrate

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

CMD ["python", "manage.py", "run_bot", "0.0.0.0:8000"]
