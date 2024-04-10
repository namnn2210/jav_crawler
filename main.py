import os

from fetch import fetch_data
from helper import read_json
from javfilm.javfilm_obj import JAVFilm
from jav4k.jav4k_obj import JAV4k
from database import get_db

root_path = os.getcwd()
print(root_path)
config = read_json(root_path)


def get_db_model(db_model_string):
    if db_model_string == 'javfilm':
        return JAVFilm(config=config)
    if db_model_string == 'jav4k':
        return JAV4k(config=config)


if __name__ == '__main__':

    db_model_config = config['db_model']
    db_model = get_db_model(db_model_config)

    start_page = config['start_page']
    end_page = config['end_page']
    list_pages = reversed(list(range(config['end_page'], config['start_page'])))
    print('DB Model:', db_model_config)
    for page_number in list_pages:
        mysql_db = get_db(config)
        print('Fetching AVDB page:', page_number)
        video_data = fetch_data(page_number)['list']
        print('Total fetch videos:', len(video_data))
        print('Pushing to DB model {}...'.format(db_model_config))
        report_data = db_model.process_data(db=mysql_db, list_video_data=video_data)
        print('Successfully added {} videos.'.format(report_data['done']['add']))
        print('Successfully update {} videos.'.format(report_data['done']['update']))
        print('Failed {} videos.'.format(report_data['error']))
        mysql_db.close()
