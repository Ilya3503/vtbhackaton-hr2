FROM python:3.12-slim

WORKDIR /app

# Копируем код и requirements
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запуск сервера
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0"]
