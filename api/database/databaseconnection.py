from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    def __init__():
        db_engine = create_engine('mysql+mysqldb://root:root@192.168.99.100:3600', pool_recycle=3600)
        db_session = scoped_session(sessionmaker(bind=engine))