from fastapi import FastAPI


# роутеры
from backend.api import vacancies

# БД
from backend.database.connection import engine, Base

# Создание таблиц (если используем SQLAlchemy без Alembic)
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="NLP HR Assistant",
    description="Backend для MVP проекта по NLP-анализу вакансий и резюме",
    version="0.1.0",
)


# подключаем роутеры
app.include_router(vacancies.router)