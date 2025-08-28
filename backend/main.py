from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


load_dotenv()

# роутеры
from backend.api import vacancies, analytics, candidates, auth

# БД
from backend.database.connection import engine, Base

# Создание таблиц (если используем SQLAlchemy без Alembic)
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="NLP HR Assistant",
    description="Backend для MVP проекта по NLP-анализу вакансий и резюме",
    version="0.1.0"
)


# подключаем роутеры
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(vacancies.router, prefix="/vacancies", tags=["vacancies"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

# Event handlers (startup/shutdown)
@app.on_event("startup")
async def startup_event():
    print("Запуск NLP HR Assistant Backend...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Выключение сервера...")
