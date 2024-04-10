from javfilm.models.genre import Genre
from slugify import slugify


def get_genre_by_name(db, name):
    genre_obj = db.query(Genre).filter(Genre.name == name).first()
    if genre_obj:
        return genre_obj.genre_id
    return 0


def get_genre_ids(db, list_genre):
    list_genre_ids = []
    for name in list_genre:
        genre_id = get_genre_by_name(db, name)
        if genre_id == 0:
            new_genre = Genre(name=name, slug=slugify(name), description='', publication=1)
            try:
                db.add(new_genre)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()

            genre_id = new_genre.genre_id
        list_genre_ids.append(str(genre_id))
    return list_genre_ids
