from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

#DB connection string
db_url = "mysql+pymysql://root@localhost:3306/fastapi"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind = engine)

