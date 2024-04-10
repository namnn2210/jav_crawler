from javfilm.models.country import Country
from slugify import slugify


def get_country_by_name(db, name):
    country_obj = db.query(Country).filter(Country.name == name).first()
    if country_obj:
        return country_obj.country_id
    return 0


def get_country_ids(db, list_country):
    list_country_ids = []
    for name in list_country:
        country_id = get_country_by_name(db, name)
        if country_id == 0:
            # Create new star
            new_country = Country(name=name, slug=slugify(name), description='', publication=1)
            try:
                db.add(new_country)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()

            country_id = new_country.country_id
        list_country_ids.append(str(country_id))
    return list_country_ids
