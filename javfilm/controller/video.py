from javfilm.models.video import Video
from javfilm.controller.star import get_star_ids
from javfilm.controller.country import get_country_ids
from javfilm.controller.genre import get_genre_ids
from javfilm.controller.episode import insert_episode
from helper import save_image_from_url
import os


def exist_video(db, tmdbid):
    return db.query(Video).filter(Video.tmdbid == tmdbid).first()


def insert_or_update_video(db, video, config):
    existed_video = exist_video(db, video['id'])
    if existed_video:
        print('Already existed video', video['slug'], '=> Updating')
        state, status = update_video(db, existed_video, video)
        return state, status
    else:
        state, status = insert_video(db, video, config)
        return state, status


def insert_video(db, video, config):
    try:
        list_actor_ids = ','.join(get_star_ids(db, video['actor'], 'actor'))
        list_director_ids = ','.join(get_star_ids(db, video['director'], 'director'))
        writer = '{}'.format(video.get('movie_code', ''))
        list_country_ids = ','.join(get_country_ids(db, video['country']))
        list_genre_ids = ','.join(get_genre_ids(db, video['category']))

        new_video = Video(
            tmdbid=video.get('id'),
            title=video.get('name', ''),
            seo_title=video.get('name', ''),
            slug=video.get('slug', ''),
            description=video.get('description', ''),
            runtime=video.get('time', ''),
            genre=list_genre_ids,
            stars=list_actor_ids,
            director=list_director_ids,
            writer=writer,
            country=list_country_ids,
            imdb_rating='n/a',
            is_tvseries=0,
            release=video.get('created_at', ''),
            video_quality='HD',
            publication=1,
            enable_download=0,
            trailler_youtube_source='',
            is_paid=0
        )
        try:
            db.add(new_video)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

        # Save thumbnail
        thumbnail_url = video.get('thumb_url', '')
        if thumbnail_url != '':
            save_image_from_url(thumbnail_url,
                                os.path.join(config.get('thumb_path'),
                                             '{}.jpg'.format(str(new_video.videos_id), '.jpg')))

        # Save poster
        poster_url = video.get('poster_url', '')
        if poster_url != '':
            save_image_from_url(thumbnail_url,
                                os.path.join(config.get('poster_path'),
                                             '{}.jpg'.format(str(new_video.videos_id), '.jpg')))

        # Episodes
        episodes = video['episodes']['server_data']
        insert_episode(db=db, video_id=new_video.videos_id, episodes=episodes)

        print('DONE ID: ', new_video.slug)
        return 'add', True
    except Exception as e:
        print(str(e))
        return 'add', False


def update_video(db, existed_video, video):
    return 'update', True
