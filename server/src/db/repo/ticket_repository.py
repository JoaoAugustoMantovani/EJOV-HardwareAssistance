from src.domain.models import Tickets
from src.db.config import DBConnectionHandler
from src.db.entities import Tickets as TicketsModel


class TicketRepository:
    """ Class to manage Ticket Repository"""
    
    @classmethod
    def insert_ticket(cls, id: int, title: str, description: str, status: str, pc_id: int, customer_id: int) -> Tickets:
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
                    status=new_ticket.status,
                    pc_id=new_ticket.pc_id,
                    customer_id=new_ticket.customer_id
                    )
                
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
                
        return None