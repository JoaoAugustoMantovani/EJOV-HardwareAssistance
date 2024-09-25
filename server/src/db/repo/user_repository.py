#pylint: disable=E1101
from typing import List 
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
    
    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]: #in future add select per role too
        """ Select data in user entity by id and/or name 
            :param - user_id: Id of registry
                   - name: User name
            :return - List with Users selected
        """
        
        try:
            query_data = None
            
            if user_id and not name:
            
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id).one()
                    query_data = [data]
                    
            elif not user_id and name:
                
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersModel).filter_by(name=name).one()
                    query_data = [data]
            
            elif user_id and name:
                
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(UsersModel).filter_by(id=user_id, name=name).one()
                    query_data = [data]
            
            return query_data
        
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
            
        return None

    