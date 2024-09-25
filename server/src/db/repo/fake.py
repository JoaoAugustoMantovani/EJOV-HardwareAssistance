# pylint: disable=E1101

from src.db.config import DBConnectionHandler
from src.db.entities import Users

class FakerRepo:
    """ A simple repository """
    
    @classmethod
    def insert_user(cls):
        """ Insert a user into the database """
        
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Joao", password="123", role="admin")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()       