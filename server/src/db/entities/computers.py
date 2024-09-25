
from datetime import datetime, timezone
import enum
from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.db.config import Base

def get_utc_now():
    return datetime.now(timezone.utc)

class Computers(Base):
    """ Users Entity """

    __tablename__ = "computers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creation_date = Column(DateTime, default=get_utc_now)
    pc_owner = Column(Integer, ForeignKey("users.id"))
