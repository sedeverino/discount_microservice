from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from app.enums.discount_type import DiscountType

# ---------- CONDITION ----------
class DiscountConditionBase(BaseModel):
    field_name: str
    operator: str
    value_condition: str
    condition_type: str

class DiscountConditionCreate(DiscountConditionBase):
    pass

class DiscountConditionUpdate(DiscountConditionBase):
    id: int

# ---------- RULE ----------
class DiscountRuleBase(BaseModel):
    value_amount: float
    min_purchase_amount: Optional[float] = None
    max_discount_amount: Optional[float] = None
    max_uses: Optional[int] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None

class DiscountRuleCreate(DiscountRuleBase):
    conditions: List[DiscountConditionCreate] = []

class DiscountRuleUpdate(DiscountRuleBase):
    id: int
    conditions: List[DiscountConditionUpdate] = []

# ---------- DISCOUNT ----------
class DiscountBase(BaseModel):
    code: str
    description: Optional[str] = None
    type: str
    active: bool = True

class DiscountFullCreate(DiscountBase):
    rules: List[DiscountRuleCreate] = []

class DiscountFullUpdate(BaseModel):
    id: int
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    active: Optional[bool] = None
    rules: List[DiscountRuleUpdate] = []

class DiscountFullResponse(DiscountBase):
    id: int
    rules: List[DiscountRuleCreate] 

    class Config:
        orm_mode = True