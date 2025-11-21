from enum import Enum

class DiscountType(str, Enum):
    PERCENTAGE = "percentage"
    FIXED = "fixed"
    USER_BIRTHDAY = "birthday"
    SEASONAL = "seasonal"