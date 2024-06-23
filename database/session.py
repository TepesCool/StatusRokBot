from sqlalchemy.orm import sessionmaker

from database.connector import engine
session = sessionmaker()
session.configure(bind=engine)
session = session()
