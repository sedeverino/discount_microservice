from sqlite3 import Date
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Enum
from app.database import Base

class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    description = Column(String)
    type = Column(Enum)  # e.g., 'percentage', 'fixed_amount'
    active = Column(Boolean, default=True)