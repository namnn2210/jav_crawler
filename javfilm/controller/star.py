from javfilm.models.star import Star
from slugify import slugify


def get_star_by_name_and_type(db, star_name, star_type):
    star_obj = db.query(Star).filter(Star.star_name == star_name, Star.star_type == star_type).first()
    if star_obj:
        return star_obj.star_id
    return 0


def get_star_ids(db, list_name, star_type):
    list_star_ids = []
    for name in list_name:
        star_id = get_star_by_name_and_type(db, name, star_type)
        if star_id == 0:
            # Create new star
            new_star = Star(star_name=name, star_type=star_type, slug=slugify(name), star_desc='', view=1, status=1)
            try:
                db.add(new_star)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()

            star_id = new_star.star_id
        list_star_ids.append(str(star_id))
    return list_star_ids
