# from database.session import session
from database.base import Base
from database.schema import Player
from database.connector import engine


class Database():
    def __init__(self):
        pass

    def create_tables(self):
        Base.metadata.create_all(engine)


obj_database = Database()
obj_database.create_tables()


