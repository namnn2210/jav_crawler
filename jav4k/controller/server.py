from jav4k.models.server import Server


def get_server_by_slug_and_src(db, slug, src):
    server_obj = db.query(Server).filter(Server.slug == slug, Server.src == src).first()
    if server_obj:
        return server_obj.id
    return 0


def insert_server(db, slug, episodes):
    episode_keys = episodes.keys()
    for episode_key in episode_keys:
        item = episodes[episode_key]
        if item['link_embed'] == '':
            continue
        server_id = get_server_by_slug_and_src(db, slug, item["slug"])
        if server_id == 0:
            server_obj = Server(
                name='HD',
                type='iframe',
                slug=slug,
                src=item["link_embed"],
            )
            try:
                db.add(server_obj)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
