from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from blog import database, models,schemas

def all_blogs(db:Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request:schemas.Blog,db:Session = Depends(database.get_db)):
    new_blog = models.Blog(title= request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    db.close()
    return new_blog

def show_blog_by_id(id,db:Session=Depends(database.get_db)):
    required_data = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not required_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog not with id {id} not found...')
    return required_data

def delete_blog(id,db:Session = Depends(database.get_db)):
    required_data = db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    if not required_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog not with id {id} not found...')
    db.commit()
    return {"blog":"Deleted"}

def update_blog(id,request:schemas.Blog,db:Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'detail with id {id} not found')
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return {'updated':'done'}