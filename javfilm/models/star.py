from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Star(Base):
    __tablename__ = 'star'

    star_id = Column(Integer, primary_key=True)
    star_type = Column(String)
    star_name = Column(String)
    slug = Column(String)
    star_desc = Column(Text)
    view = Column(Integer)
    status = Column(Integer)
