from faker import Faker
from sqlalchemy import text
from src.db.config import DBConnectionHandler
from src.db.entities.users import Roles
from .user_repository import UserRepository
from src.db.entities import Users as UsersModel

faker = Faker()
db_connection_handler = DBConnectionHandler()
user_repository = UserRepository()

roles = ['admin', 'user', 'support']

def test_insert_user():
    """ Should insert user """
    
    
    
    name = faker.name()
    password = faker.word()
    role = faker.random_element(elements=roles)
    
    #SQL Commands
    new_user = user_repository.insert_user(name,password,role)
    
    engine = db_connection_handler.get_engine()
    with engine.connect() as connection:
        query = text("SELECT * FROM users WHERE id=:id")
        query_user = connection.execute(query, {"id": new_user.id}).fetchone()
    
    
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
    assert new_user.role == Roles[query_user.role]
    
    # Insert later a query to delete de data wrote on DB
    
def test_select_user():
    """ Should select a user in Users table and compare it """
    
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    role = faker.random_element(elements=roles)
    data = UsersModel(id=user_id, name=name, password=password, role=role)
    
    engine = db_connection_handler.get_engine()
    with engine.connect() as connection:
        query = text("INSERT INTO users (id, name, password, role) VALUES (:id, :name, :password, :role);")
        query_user = connection.execute(query, {"id": user_id, "name": name, "password": password, "role": role})
        connection.commit()
    
    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)
    
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3
    
    # Insert later a query to delete de data wrote on DB