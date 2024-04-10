from googletrans import Translator

translator = Translator()


def translate_data(data, source_lang, target_lang):
    try:
        return translator.translate(data, src=source_lang, dest=target_lang)
    except Exception as ex:
        return None


def process_translate(video, source_lang, target_lang):
    if target_lang != "en":
        # Translate name
        translated_name = translate_data(video['name'], source_lang=source_lang, target_lang=target_lang)
        if translated_name:
            video['name'] = translated_name.text
        # Translate origin name
        translated_origin_name = translate_data(video['origin_name'], source_lang=source_lang,
                                                target_lang=target_lang)
        if translated_origin_name:
            video['origin_name'] = translated_origin_name.text
        # Description
        translated_description = translate_data(video['description'], source_lang=source_lang,
                                                target_lang=target_lang)
        if translated_description:
            video['description'] = translated_description.text
    return video
