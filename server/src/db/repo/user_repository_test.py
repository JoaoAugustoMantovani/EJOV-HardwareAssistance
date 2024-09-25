from faker import Faker
from sqlalchemy import text
from src.db.config import DBConnectionHandler
from src.db.entities.users import Roles
from .user_repository import UserRepository


faker = Faker()
db_connection_handler = DBConnectionHandler()
user_repository = UserRepository()


def test_insert_user():
    """ Should insert user """
    
    roles = ['admin', 'user', 'support']
    
    name = faker.name()
    password = faker.word()
    role = faker.random_element(elements=roles)
    engine = db_connection_handler.get_engine()
    
    
    #SQL Commands
    new_user = user_repository.insert_user(name,password,role)
    
    # with engine.connect() as connection:
    #     query = text("SELECT * FROM users WHERE id=:id")
    #     query_user = connection.execute(query, {"id": new_user.id}).fetchone()
    
    # print(new_user)
    # print(query_user)
    
    # assert new_user.id == query_user.id
    # assert new_user.name == query_user.name
    # assert new_user.password == query_user.password
    # assert new_user.role == Roles[query_user.role]
    
    
    