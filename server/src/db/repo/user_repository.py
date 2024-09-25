#pylint: disable=E1101 
from src.domain.models import Users
from collections import namedtuple
from src.db.config import DBConnectionHandler
from src.db.entities import Users as UsersModel

class UserRepository:
    """ Class to manage User Repository"""
    
    @classmethod
    def insert_user(cls, name: str, password:str, role: str) -> Users:
        """Insert a new user into the database
        :param - name: person name
               - password: user password
               - role: user role
        :return - tuple with new user inserted
        """
        
        
        
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password, role=role)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                
                return Users(id=new_user.id, name=new_user.name, password=new_user.password, role=new_user.role)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        
        return None