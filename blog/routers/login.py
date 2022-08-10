from importlib.resources import contents
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from blog import database,models,hashing
from fastapi import APIRouter,Depends, HTTPException,status
from blog.JWTtoken import create_access_token
router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="invalid Credientials")
    if hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="invalid Password")

    access_token = create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}