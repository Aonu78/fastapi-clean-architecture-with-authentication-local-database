from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# from motor.motor_asyncio import AsyncIOMotorClient

# DB_URL="mongodb://aonu:aonu@cluster0-shard-00-00.bty5q.mongodb.net:27017,cluster0-shard-00-01.bty5q.mongodb.net:27017,cluster0-shard-00-02.bty5q.mongodb.net:27017/test?replicaSet=atlas-n4iwun-shard-0&ssl=true&authSource=admin"

# async def get_database() -> AsyncIOMotorClient:
#     client: AsyncIOMotorClient = None
#     client = AsyncIOMotorClient(DB_URL)
#     db = client['user']
#     return db







# engine = create_engine('sqlite:///./blog.db',echa=True)
SQLALCAMY_DATABASE_URL = 'sqlite:///./blog/blog.db'
engine = create_engine(SQLALCAMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

