from sqlite3 import Date
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Enum
from app.database import Base

class DiscountRule(Base):
    __tablename__ = "discount_rules"

    id = Column(Integer, primary_key=True, index=True)
    rule_counter = Column(Integer, default=0)
    discount_id = Column(Integer)
    value_amount = Column(Float)
    min_purchase_amount = Column(Float)
    max_discount_amount = Column(Float)
    max_uses = Column(Integer)
    uses_count = Column(Integer, default=0)
    valid_from = Column(Date)  # start date
    valid_to = Column(Date)    # end date