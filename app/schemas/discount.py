from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from app.enums.discount_type import DiscountType


# ===============================================================
#                    CONDITION SCHEMAS
# ===============================================================

class DiscountConditionCreate(BaseModel):
    field_name: str                 
    operator: str                   
    value_condition: str            
    condition_type: str             


# ===============================================================
#                    RULE SCHEMAS
# ===============================================================

class DiscountRuleCreate(BaseModel):
    value_amount: float
    min_purchase_amount: Optional[float] = None
    max_discount_amount: Optional[float] = None
    max_uses: Optional[int] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None

    # Cada regla puede tener 0..N condiciones
    conditions: List[DiscountConditionCreate] = []


# ===============================================================
#                    DISCOUNT SCHEMAS
# ===============================================================

class DiscountCreate(BaseModel):
    code: str
    description: Optional[str] = None
    type: DiscountType                       # "percentage", "fixed_amount"
    active: bool = True


class DiscountFullCreate(DiscountCreate):
    """
    Extiende el schema base DiscountCreate,
    agregando todas las reglas + condiciones.
    """
    rules: List[DiscountRuleCreate] = []
