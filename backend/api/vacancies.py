from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# Простейший in-memory "хранилище" для MVP
vacancies_db = []

# Эндпоинт 1: создание вакансии
@router.post("/vacancies")
def create_vacancy(title: str):
    vacancy_id = len(vacancies_db) + 1
    vacancy = {"id": vacancy_id, "title": title}
    vacancies_db.append(vacancy)
    return vacancy

# Эндпоинт 2: получить все вакансии
@router.get("/vacancies", response_model=List[dict])
def get_vacancies():
    return vacancies_db
