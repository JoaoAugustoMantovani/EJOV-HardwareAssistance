from datetime import datetime
from zoneinfo import ZoneInfo
import enum
from sqlalchemy import Column, String, Integer, Date, Enum, DateTime
from sqlalchemy.orm import relationship
from src.db.config import Base

def get_local_now():
    local_tz = ZoneInfo('America/Sao_Paulo')  # Altere para o seu fuso horário
    return datetime.now(local_tz)

class Roles(enum.Enum):
    """" Defining Users Roles """

    admin = "admin"
    support = "support"
    user = "user"
    
class Users(Base):
    """ Users Entity """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(Enum(Roles), nullable=False)
    password = Column(String, nullable=False)
    birthdate = Column(Date, nullable=True)
    creation_date = Column(DateTime, default=get_local_now)
    #After insertion of birthdate on register page, modify the 'nullable=True' to 'nullable=False'

    def __rep__(self):
        return f"User [name={self.name}, role={self.role}, birthdate={self.birthdate}]"
    
    def __eq__(self, other):
        if (
            self.id == other.id 
            and self.name == other.name 
            and self.password == other.password
            ):
            return True
        return False