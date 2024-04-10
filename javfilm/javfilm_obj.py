from translater import process_translate
from javfilm.controller.video import insert_or_update_video


class JAVFilm:
    def __init__(self, config):
        self.config = config

    def process_data(self, db, list_video_data):
        return self.insert_to_db(db, list_video_data)

    def insert_to_db(self, db, list_video_data):
        report_data = {
            'total': 0,
            'done': {
                'add': 0,
                'update': 0
            },
            'error': 0
        }
        source_lang = self.config['source_lang']
        target_lang = self.config['target_lang']
        for video_data in list_video_data:
            try:
                translated_video_data = process_translate(video_data, source_lang=source_lang, target_lang=target_lang)
                state, status = insert_or_update_video(db, translated_video_data, config=self.config)
                if state == 'add' and status:
                    report_data['done']['add'] += 1
                if state == 'update' and status:
                    report_data['done']['update'] += 1
            except Exception as e:
                print(str(e))
                report_data['error'] += 1
        return report_data
