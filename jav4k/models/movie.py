from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(1000), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    url = Column(String(255), nullable=False, unique=True)
    code_prefix = Column(String(255))
    description = Column(Text)
    categories = Column(Text)
    tags = Column(Text)
    thumbnail = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())
    views = Column(BigInteger, nullable=False, default=0)
    views_in_day = Column(BigInteger, nullable=False, default=0)
    fake_views = Column(BigInteger, nullable=False, default=100000)
