from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from blog import database,models,schemas, hashing

def cerate_user(request:schemas.User,db:Session = Depends(database.get_db)):
    new_user = models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(id,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()   
    if not user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'User with id {id} is note available')
    return user