from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    def __init__(self):
        self.db_engine = create_engine('mysql+pymysql://root:root@192.168.99.100:3306/hris-db', pool_recycle=3600)
        self.db_session = scoped_session(sessionmaker(bind=self.db_engine))

        self.base = declarative_base()
        self.base.query = self.db_session.query_property()
