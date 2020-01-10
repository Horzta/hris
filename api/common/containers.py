from dependency_injector.providers import Singleton
from dependency_injector.containers import DeclarativeContainer
from database.databaseconnection import DatabaseConnection

class Databases(DeclarativeContainer):
    default_conn = Singleton(DatabaseConnection)
