import enum
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.db.config import Base

def get_utc_now():
    return datetime.now(timezone.utc)

class Status(enum.Enum):
    """" Defining Users Roles """

    closed = "closed"
    in_progress = "in_progress"
    active= "active"
    
class Tickets(Base):
    """ Ticket Entity """

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String,)
    status = Column(Enum(Status), nullable=False)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pc_id = Column(Integer, ForeignKey("computers.id"), nullable=False)
    creation_date = Column(DateTime, default=get_utc_now)
    #After insertion of birthdate on register page, modify the 'nullable=True' to 'nullable=False'

    def __rep__(self):
        return f"ticket [name={self.ticket}]"
    