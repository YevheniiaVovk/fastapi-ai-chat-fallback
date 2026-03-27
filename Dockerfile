FROM python:3.13-slim

# Встановлюємо uv прямо в контейнер
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Копіюємо файли залежностей (це прискорює білд)
COPY pyproject.toml uv.lock ./

# Встановлюємо залежності без створення окремого venv всередині контейнера
RUN uv sync --frozen --no-cache

# Копіюємо решту коду
COPY . .

# Експортуємо порт для FastAPI
EXPOSE 8000

# Команда запуску
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]