from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth import create_user, authenticate_user, create_access_token

router = APIRouter()

@router.post("/register")
def register_user(username: str, password: str):
    user = create_user(username, password)
    return {"message": "Пользователь создан", "user_id": user.id}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Неверные данные")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_current_user(current_user=Depends(authenticate_user)):
    return {"username": current_user.username, "id": current_user.id}
