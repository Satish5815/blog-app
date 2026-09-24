from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.services.user_service import getUserById,createUser
from app.database import get_db

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)

# @router.get('/')
# def get_user():
#  return {"message":"Get All use"}

@router.get('/{user_id}')
def get_user(user_id:str,db:Session=Depends(get_db)):
    user=getUserById(user_id,db)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User does not exist"
        )
    
    return {
        "status":"Success",
        "user":user
    }    
    

@router.post('/signin/')
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    user=createUser(user,db)
    if not user:
        raise HTTPException(
            status_code=409,
            detail="Email already Exist"
        )
    
    return {
        "status":"User hash been created",
        "user":user
    }

@router.post('/login')
def user_login():
    return {"message":"Hello from login router"}        