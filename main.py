from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog,user,login

app = FastAPI()

models.Base.metadata.create_all(engine) 

@app.get("/")
def default():
    return {"Hell Dear": "Well Come to Latest Defined API on Fastapi framwork"}

app.include_router(login.router)
app.include_router(user.router)
app.include_router(blog.router)


# from fastapi import FastAPI,Depends
# from typing import Optional
# from motor.motor_asyncio import AsyncIOMotorClient
# app = FastAPI()

# DB_URL="mongodb://aonu:aonu@cluster0-shard-00-00.bty5q.mongodb.net:27017,cluster0-shard-00-01.bty5q.mongodb.net:27017,cluster0-shard-00-02.bty5q.mongodb.net:27017/test?replicaSet=atlas-n4iwun-shard-0&ssl=true&authSource=admin"

# async def get_database() -> AsyncIOMotorClient:
#     client: AsyncIOMotorClient = None
#     client = AsyncIOMotorClient(DB_URL)
#     db = client['user']
#     return db

# @app.post("/")
# def default():
#     return {"Well come","User"}

# @app.post("/insert_user/{Auth_Name}")
# async def insert_record(db:AsyncIOMotorClient = Depends(get_database),Auth_Name : str=None,Book_Name : Optional[str]=None):
#     record_dict = {"Author":Auth_Name,"Book":Book_Name}
#     db.test_collection.insert_one(record_dict)
#     return {"data":"inserted"}


