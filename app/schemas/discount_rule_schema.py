from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from app.schemas.condition_schema import DiscountConditionCreate, DiscountConditionUpdate

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