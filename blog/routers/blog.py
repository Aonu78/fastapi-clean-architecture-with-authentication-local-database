from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import Authentication
from blog import database, schemas
from blog.repository import blog as blog
from motor.motor_asyncio import AsyncIOMotorClient
router = APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all_blogs(db:Session = Depends(database.get_db), get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return blog.all_blogs(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session = Depends(database.get_db), get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return blog.create_blog(request,db)
    

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db:Session = Depends(database.get_db), get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return blog.show_blog_by_id(id,db)

@router.delete('/{id}')
def destroy(id,db:Session = Depends(database.get_db), get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return blog.delete_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(database.get_db), get_current_user : schemas.User = Depends(Authentication.get_current_user)):
    return blog.update_blog(id,request,db)

