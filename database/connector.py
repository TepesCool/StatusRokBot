from sqlalchemy import create_engine
from constants.constant import DB_HOST, DB_PORT, DB_SCHEMA, DB_PASSWORD, DB_USERNAME

engine = create_engine(f"mariadb+mariadbconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}")
