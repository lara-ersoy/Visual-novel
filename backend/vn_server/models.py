from sqlalchemy import Column, Integer, String, JSON
from .db import Base

class Scene(Base):
    __tablename__ = "scenes"
    id = Column(Integer, primary_key = True)
    slug = Column(String, unique= True)
    title = Column(String)
    script = Column(JSON)