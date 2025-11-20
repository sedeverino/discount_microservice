from sqlite3 import Date
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Enum
from app.database import Base

class DiscountUsage(Base):
    __tablename__ = "discount_usage"

    id = Column(Integer, primary_key=True, index=True)
    discount_id = Column(Integer)
    user_id = Column(Integer)
    order_id = Column(Integer)
    used_at = Column(Date)
    discounted_amount = Column(Float)