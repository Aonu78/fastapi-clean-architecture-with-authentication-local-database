from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from blog import database,models,schemas, hashing
from blog.repository import user
from blog import Authentication
from motor.motor_asyncio import AsyncIOMotorClient


router = APIRouter(
    tags=['User'],
    prefix="/user"
)

@router.post('/')
def create_user(request:schemas.User,db:Session = Depends(database.get_db)):
    return user.cerate_user(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id,db:Session = Depends(database.get_db), get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return user.get_user_by_id(id,db)

@router.get("/")
def get_current_user(get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return {"current user":get_current_user}