
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.db_models import User
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.core.security import get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

auth_router = APIRouter()



@auth_router.post("/registration", response_model=UserResponse)
def user_registration(data: UserCreate, db: Session = Depends(get_db)):
    
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    
    hashed_pw = get_password_hash(data.password)
    
    
    new_user = User(
        email=data.email, 
        hashed_password=hashed_pw,
        username=data.username  
    )
    
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@auth_router.post("/login")
def user_loging(form_data: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if user:
        if verify_password(form_data.password, user.hashed_password):
            token = create_access_token(data={"sub": user.email})
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
