from sqlite3 import Date
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Enum
from app.database import Base

class Condition(Base):
    __tablename__ = "discount_condition"

    id = Column(Integer, primary_key=True, index=True)
    discount_rule_id = Column(Integer)
    field_name = Column(String)  # e.g.,        'user_type',        'purchase_date'
    operator = Column(Enum)    # e.g.,          'equals',           'greater_than'
    value_condition = Column(String) # e.g.,    'premium',          '2024-12-25'
    condition_type = Column(Enum)  # e.g.,      'first_time_user',  'holiday_special'