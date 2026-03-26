from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.router import router
from app.models import db_models
from app.api.auth import auth_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Server is running. Database initialized."}

