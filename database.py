import os
from sqlalchemy import create_engine



# Load credentials
userEnv = open(os.getenv("MARIADB_USER_FILE")).read()
passwordEnv = open(os.getenv("MARIADB_PASSWORD_FILE")).read()
databaseEnv = open(os.getenv("MARIADB_DATABASE_FILE")).read()


engine = create_engine(f"mysql+pymysql://{userEnv}:{passwordEnv}@db/{databaseEnv}", echo=True, future=True)

