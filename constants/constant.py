import os

# ==========DB CONSTANTS================ #
DB_HOST = os.environ["DB_HOST"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PORT = os.environ["DB_PORT"]
DB_SCHEMA = os.environ["DB_SCHEMA"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
# ==========DB CONSTANTS================ #
print(DB_SCHEMA)