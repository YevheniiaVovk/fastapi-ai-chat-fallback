from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.db_models import User
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = decoded.get("sub")
      
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if email is None: 
        raise HTTPException(status_code=401, detail="Email does not exist")
    user = db.query(User).filter(User.email==email).first()
    if user is None: 
        raise HTTPException(status_code=401, detail="User does not exist")
    return user


