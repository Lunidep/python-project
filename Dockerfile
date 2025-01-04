# Используем базовый образ Python 3.8
FROM python:3.8
ENV PYTHONUNBUFFERED=1

# Устанавливаем системные зависимости, включая distutils
RUN apt-get update && apt-get install -y \
    python3-distutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Если requirements.txt нет, устанавливаем Django напрямую
RUN pip install django==3.2  # или любую нужную вам версию

# Применяем миграции базы данных
RUN python manage.py migrate

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]