from javfilm.models.episode import VideoFile, Season, Episode
from helper import generate_random_string
from datetime import datetime


def insert_episode(db, video_id, episodes):
    episode_keys = episodes.keys()
    if len(episode_keys) > 1:
        season_obj = Season(
            videos_id=video_id,
            seasons_name='Season 1',
            order=0,
        )
        try:
            db.add(season_obj)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

        for episode_key in episode_keys:
            item = episodes[episode_key]
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
            if item['link_embed'] == '':
                continue
            episode_obj = Episode(
                videos_id=video_id,
                seasons_id=season_obj.seasons_id,
                episodes_name=item["slug"],
                order=0,
                date_added=formatted_datetime,
                stream_key=generate_random_string(),
                file_source='embed',
                file_url=item['link_embed'],
                source_type='link',
            )
            try:
                db.add(episode_obj)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
    else:
        for episode_key in episode_keys:
            item = episodes[episode_key]
            # Insert to video file
            video_file = VideoFile(
                videos_id=video_id,
                stream_key=generate_random_string(),
                file_source='embed',
                source_type='link',
                file_url=item['link_embed'],
                label=item['slug'],
                order=0
            )
            try:
                db.add(video_file)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()