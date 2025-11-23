from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.condition import Condition
from app.schemas.condition_schema import DiscountConditionCreate, DiscountConditionUpdate

class ConditionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: DiscountConditionCreate) -> Condition:
        condition = Condition(**data.model_dump(exclude_none=True))
        self.session.add(condition)
        await self.session.commit()
        await self.session.refresh(condition)
        return condition

    async def get_by_id(self, id: int) -> Condition | None:
        return await self.session.get(Condition, id)

    async def get_by_rule_id(self, rule_id: int) -> list[Condition]:
        result = await self.session.execute(
            select(Condition).where(Condition.discount_rule_id == rule_id)
        )
        return result.scalars().all()

    async def list(self) -> list[Condition]:
        result = await self.session.execute(select(Condition))
        return result.scalars().all()

    async def update(self, condition: Condition, data: DiscountConditionUpdate) -> Condition:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(condition, key, value)
        self.session.add(condition)
        await self.session.commit()
        await self.session.refresh(condition)
        return condition

    async def delete(self, condition: Condition):
        await self.session.delete(condition)
        await self.session.commit()
        return 1

