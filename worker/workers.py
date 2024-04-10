# from celery import Celery
# from helper import read_json
# from javfilm.javfilm_obj import JAVFilm
# from jav4k.jav4k_obj import JAV4k
# import os
#
# root_path = os.getcwd()
# print(root_path)
# config = read_json(root_path)
#
# REDIS_PASSWORD = config['redis']['password']
# REDIS_HOST = config['redis']['host']
# REDIS_PORT = config['redis']['port']
# REDIS_DB = config['redis']['db']
# app = Celery('JAV Crawler Queue', broker=f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}')
#
#
# def get_db_model(db_model_string):
#     if db_model_string == 'javfilm':
#         return JAVFilm(config=config)
#     if db_model_string == 'jav4k':
#         return JAV4k(config=config)
#
#
# @app.task(name='process_crawl')
# def process_crawl(db, list_video_data):
#     db_model_config = config['db_model']
#     db_model = get_db_model(db_model_config)
#     connector = get_connector(original)
#     if connector:
#         connector.get_metadata(manga=manga)
