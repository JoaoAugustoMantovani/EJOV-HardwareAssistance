from faker import Faker
from sqlalchemy import text
from unittest.mock import MagicMock
from src.db.config import DBConnectionHandler
from src.db.entities.tickets import Status
from src.db.entities import Tickets
from .ticket_repository import TicketRepository


faker = Faker()
ticket_repository = TicketRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_ticket():
    """ Should insert ticket table and return it """
    
    #Mocks
    mock_customer = MagicMock()
    mock_customer.id = faker.random_number(digits=4)

    mock_computer = MagicMock()
    mock_computer.id = faker.random_number(digits=4)
    
    #Ticket data
    ticket_id = faker.random_number(digits=4)  
    title = faker.text(max_nb_chars=30)
    description = faker.text(max_nb_chars=180)
    status = 'active'  
    customer_id = mock_customer.id
    pc_id = mock_computer.id
    
    
    
    #SQL Commands
    
    new_ticket = ticket_repository.insert_ticket(ticket_id, title, description, status, pc_id, customer_id)
    engine = db_connection_handler.get_engine()
    with engine.connect() as connection:
        query = text("SELECT * FROM tickets WHERE id=:id")
        query_ticket = connection.execute(query, {"id": new_ticket.id}).fetchone()
        
        
    print("\n\n",new_ticket)    
    print(query_ticket)
    
    assert new_ticket.id == ticket_id
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
    finally:
        db_connection.session.close()
        

def test_select_ticket():
    """ Should select a ticket in Tickets table and compare it"""
    
   #Mocks
    mock_customer = MagicMock()
    mock_customer.id = faker.random_number(digits=4)

    mock_computer = MagicMock()
    mock_computer.id = faker.random_number(digits=4)
    
    #Ticket data
    id = faker.random_number(digits=4)  
    title = faker.text(max_nb_chars=30)
    description = faker.text(max_nb_chars=180)
    status = "active"  
    customer_id = mock_customer.id
    pc_id = mock_computer.id
    
    status_mock = Status("active")
    data = Tickets(id=id, title=title, description=description, status=status_mock, pc_id=pc_id, customer_id=customer_id)
    
    #SQL Commands
    
    engine = db_connection_handler.get_engine()
    with engine.connect() as connection:
        query = text("INSERT INTO tickets (id, title, description, status, pc_id, customer_id) VALUES (:id, :title, :description, :status, :pc_id, :customer_id)")
        query_ticket = connection.execute(query, {"id": id,"title": title, "description": description, "status": status, "pc_id": pc_id, "customer_id": customer_id})
        connection.commit()
        
        query_select = text("SELECT * FROM tickets WHERE id=:id")
        query_ticket = connection.execute(query_select, {"id": id}).fetchone()
    
    query_tickets1 = ticket_repository.select_ticket(id=id)
    query_tickets2 = ticket_repository.select_ticket(title=title) 
    query_tickets3 = ticket_repository.select_ticket(description=description)
    query_tickets4 = ticket_repository.select_ticket(status=status) 
    query_tickets5 = ticket_repository.select_ticket(pc_id=pc_id) 
    query_tickets6 = ticket_repository.select_ticket(customer_id=customer_id)      
    
    assert data.id == query_tickets1[0].id
    assert data.title == query_tickets1[0].title
    assert data.description == query_tickets1[0].description
    assert data.status == query_tickets1[0].status
    assert data.pc_id == query_tickets1[0].pc_id
    assert data.customer_id == query_tickets1[0].customer_id
    
    with engine.connect() as connection:
        try:
            query = text("DELETE FROM users where id=:id")
            query_user = connection.execute(query, {"id": id})
            connection.commit()
        except:
            db_connection_handler.session.rollback()
            raise
     
        