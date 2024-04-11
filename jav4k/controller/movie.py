from jav4k.models.movie import Movie
from jav4k.controller.server import insert_server
from helper import generate_random_string
from helper import save_image_from_url
import random
import os

def exist_video(db, slug):
    return db.query(Movie).filter(Movie.slug == slug).first()


def insert_or_update_video(db, video, config):
    existed_video = exist_video(db, video['slug'])
    if existed_video:
        state, status = update_video(db, existed_video, video)
        return state, status
    else:
        state, status = insert_video(db, video, config)
        return state, status


def insert_video(db, video, config):
    try:

        new_video = Movie(
            name=video.get('name', ''),
            slug=video.get('slug', ''),
            url=generate_random_string(),
            code_prefix=video.get('movie_code', ''),
            description=video.get('description', ''),
            categories=','.join(video.get('category')),
            tags=','.join(video.get('actor')),
            thumbnail=video.get('thumb_url', ''),
            fake_views=random.randint(50000, 200000)
        )
        try:
            db.add(new_video)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

        thumbnail_url = video.get('thumb_url', '')
        if thumbnail_url != '':
            save_image_from_url(thumbnail_url,
                                os.path.join(config.get('thumb_path'),
                                             '{}.jpg'.format(str(Movie.id), '.jpg')))

        # Episodes
        episodes = video['episodes']['server_data']
        insert_server(db=db, slug=video.get('slug', ''), episodes=episodes)
        print('DONE ID ', new_video.slug)
        return 'add', True
    except Exception as e:
        print(str(e))
        return 'add', False


def update_video(db, existed_video, video):
    return 'update', True
