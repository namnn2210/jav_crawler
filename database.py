from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db(config):
    # Define the database URL
    DB_URL = 'mysql://{}:{}@{}:{}/{}'.format(config['database']['mysql']['username'],
                                             config['database']['mysql']['password'],
                                             config['database']['mysql']['host'], config['database']['mysql']['port'],
                                             config['database']['mysql']['db_name'])

    # Create the SQLAlchemy engine
    engine = create_engine(DB_URL)

    # Create a session factory
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
