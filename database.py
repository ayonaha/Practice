import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# TODO Hack to test the MySQL environment variable query string
# DB_URL = "mysql+pymysql://myuser:mypassword@localhost/mydatabase"
DB_URL = os.getenv('DATABASE_URL', 'sqlite:///todo.sqlite3')

engine = create_engine(DB_URL)  # , connect_args={'check_same_thread': False})
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()