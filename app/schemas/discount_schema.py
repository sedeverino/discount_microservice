from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from app.schemas.discount_rule_schema import DiscountRuleCreate, DiscountRuleUpdate

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