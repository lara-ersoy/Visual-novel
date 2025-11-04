from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///vn.db" 
engine = create_engine(DATABASE_URL, echo = False, future= True)
SessionLocal = sessionmaker(bind = engine, expire_on_commit=False, future=True)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind = engine)