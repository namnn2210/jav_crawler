from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Genre(Base):
    __tablename__ = 'genre'

    genre_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    slug = Column(String)
    publication = Column(Integer)
    featured = Column(Integer, default=0)
