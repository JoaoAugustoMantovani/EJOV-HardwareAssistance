from faker import Faker
from .ticket_repository import TicketRepository
from src.db.config import DBConnectionHandler
from sqlalchemy import text
from unittest.mock import MagicMock

faker = Faker()
ticket_repository = TicketRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_ticket():
    """ Should insert ticket table and return it """
    
    #Mocks
    mock_customer = MagicMock()
    mock_customer.id = faker.random_number()

    mock_computer = MagicMock()
    mock_computer.id = faker.random_number()
    
    #Ticket data
    id = faker.random_number()  # Gerando um ID falso
    title = faker.text(max_nb_chars=30)
    description = faker.text(max_nb_chars=180)
    status = 'active'  # Forneça um status válido
    customer_id = mock_customer.id
    pc_id = mock_computer.id
    
    
    
    #SQL Commands
    
    new_ticket = ticket_repository.insert_ticket(id, title, description, status, pc_id, customer_id)
    engine = db_connection_handler.get_engine()
    with engine.connect() as connection:
        query = text("SELECT * FROM tickets WHERE id=:id")
        query_ticket = connection.execute(query, {"id": new_ticket.id}).fetchone()
        
        
    print("\n\n",new_ticket)    
    print(query_ticket)
    
    assert new_ticket.id == id
    assert new_ticket.title == title
    assert new_ticket.description == description
    assert new_ticket.status.value == status
    assert new_ticket.pc_id == pc_id
    assert new_ticket.customer_id == customer_id
    
    #DB Clean
    
    with DBConnectionHandler() as db_connection:
        session = db_connection.session
    try:
        query = text("DELETE FROM tickets WHERE id=:id")
        session.execute(query, {"id": new_ticket.id})
        session.commit()  
    except:
        session.rollback() 
        raise
    