from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    total = Column(DECIMAL(8, 2), nullable=False)
    show_on_menu = Column(Boolean, nullable=False, default=False)
    show_on_homepage = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())
