from typing import List
from src.domain.models import Tickets
from src.db.config import DBConnectionHandler
from src.db.entities import Tickets as TicketsModel


class TicketRepository:
    """ Class to manage Ticket Repository"""
    
    @classmethod
    def insert_ticket(cls, id: int, title: str, description: str, status: str, pc_description: str, customer_id: int) -> Tickets:
        """ 
        Insert data in TicketsEntity entity
        :param - title: a ticket brief
               - description: entire ticket explanation
               - status: ticket status (active, in_progress, closed)
               - pc_id: id of the PC that the ticket is related to (FK)
               - customer_id: id of the customer that the ticket is related to (FK)
        :return - tuple with new ticket inserted
        """
        
        with DBConnectionHandler() as db_connection:
            try:
                new_ticket = TicketsModel(id=id, title=title, description=description, status=status, pc_id=pc_id, customer_id=customer_id)
                db_connection.session.add(new_ticket)
                db_connection.session.commit()
                
                return Tickets(
                    id=new_ticket.id,
                    title=new_ticket.title,
                    description=new_ticket.description,
                    pc_description=new_ticket.pc_description,
                    status=new_ticket.status,
                    customer_id=new_ticket.customer_id
                    )
                
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
                
        return None
    
    def select_ticket (cls, id: int = None,  title: str = None, description: str = None, status:str = None,customer_id: int = None, pc_description: str = None) -> List[Tickets]:
        """
        Select data in TicketsEntity entity by ticket_id and/or user_id
        :param - ticket_id: ticket id registered
               - user_id: customer id registered
        :return - List with tickets selected     
        """
        with DBConnectionHandler() as db_connection:
            try:
                
                query_data = None
                
                if id and not customer_id:
                
                    with DBConnectionHandler() as db_connection:
                        data = db_connection.session.query(TicketsModel).filter_by(id=id).one()
                        query_data = [data]
                        
                elif not id and customer_id:
                    
                    with DBConnectionHandler() as db_connection:
                        data = db_connection.session.query(TicketsModel).filter_by(customer_id=customer_id).all()
                        query_data = data
                
                elif id and customer_id:
                    
                    with DBConnectionHandler() as db_connection:
                        data = db_connection.session.query(TicketsModel).filter_by(id=id, customer_id=customer_id).one()
                        query_data = [data]
                
                return query_data
            
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            
            return None
            
        
        
            
      