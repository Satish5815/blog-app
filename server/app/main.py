from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.database import get_db,Base,engine
from app.router import router as UserRouter

app=FastAPI()
#if db is not exist then it will create a db
Base.metadata.create_all(bind=engine)

app.include_router(UserRouter)

@app.get('/')
def health_check():
    return{
        "message":"Health checkup api"
    }




