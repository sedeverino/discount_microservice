from pydantic import BaseModel
from typing import Optional

class DiscountConditionBase(BaseModel):
    field_name: str
    operator: str
    value_condition: str
    condition_type: str

class DiscountConditionCreate(DiscountConditionBase):
    pass

class DiscountConditionUpdate(DiscountConditionBase):
    id: int