from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Episode(Base):
    __tablename__ = 'episodes'

    episodes_id = Column(Integer, primary_key=True)
    stream_key = Column(String)
    videos_id = Column(Integer)
    seasons_id = Column(Integer)
    episodes_name = Column(String)
    file_source = Column(String)
    source_type = Column(String)
    file_url = Column(String)
    order = Column(Integer)
    date_added = Column(String)
    last_ep_added = Column(String, default='')


class VideoFile(Base):
    __tablename__ = 'video_file'

    video_file_id = Column(Integer, primary_key=True)
    stream_key = Column(String)
    videos_id = Column(Integer)
    file_source = Column(String)
    source_type = Column(String)
    file_url = Column(String)
    label = Column(String)
    order = Column(Integer)


class Season(Base):
    __tablename__ = 'seasons'

    seasons_id = Column(Integer, primary_key=True)
    videos_id = Column(Integer)
    seasons_name = Column(String(250))
    order = Column(Integer, default=0)
    publish = Column(Integer, default=1)
