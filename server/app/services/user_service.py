
from sqlalchemy.orm import Session
from fastapi import HTTPException
import uuid

from app.model.user_model import User as UserModel
from app.schemas.user_schema import UserCreate,UserLogin
from app.core import hash_password,verify_password

def getUserById(id:str,db:Session):
    user=db.get(UserModel,id)
    return user
# def getAllUser(db:Session):
#     return db.getA

def createUser(user_data:UserCreate,db:Session):  
    existing_user=(
        db.query(UserModel)
        .filter(UserModel.email==user_data.email)
        .first()
    )
    if existing_user:
        return None
    hashed_password = hash_password(user_data.password)
    
    user=UserModel(
        id=str(uuid.uuid4()),
        name=user_data.name,
        email=user_data.email,
        password_hash=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def userLogin(loginData:UserLogin,db:Session):
    user=(
        db.query(UserModel)
        .filter(UserModel.email==loginData.email)
        .first()
    )
    