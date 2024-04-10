from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Video(Base):
    __tablename__ = 'videos'

    videos_id = Column(Integer, primary_key=True)
    imdbid = Column(String)
    tmdbid = Column(String)
    title = Column(String)
    seo_title = Column(String)
    slug = Column(String)
    description = Column(Text)
    stars = Column(String)
    director = Column(String)
    writer = Column(String)
    rating = Column(String)
    release = Column(String)
    country = Column(String)
    genre = Column(String)
    language = Column(String)
    video_type = Column(String)
    runtime = Column(String)
    video_quality = Column(String)
    is_paid = Column(Integer)
    publication = Column(Integer)
    trailer = Column(Integer)
    trailler_youtube_source = Column(String)
    enable_download = Column(Integer)
    focus_keyword = Column(String)
    meta_description = Column(String)
    tags = Column(String)
    imdb_rating = Column(String)
    is_tvseries = Column(Integer)
    total_rating = Column(Integer)
    today_view = Column(Integer)
    weekly_view = Column(Integer)
    monthly_view = Column(Integer)
    total_view = Column(Integer)
    last_ep_added = Column(String)
