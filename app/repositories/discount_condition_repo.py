from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.discount_condition import DiscountCondition

class DiscountConditionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> DiscountCondition:
        condition = DiscountCondition(**data)
        self.session.add(condition)
        await self.session.commit()
        await self.session.refresh(condition)
        return condition

    async def get_by_id(self, id: int) -> DiscountCondition | None:
        return await self.session.get(DiscountCondition, id)

    async def get_by_rule_id(self, rule_id: int) -> list[DiscountCondition]:
        result = await self.session.execute(
            select(DiscountCondition).where(DiscountCondition.discount_rule_id == rule_id)
        )
        return result.scalars().all()

    async def list(self) -> list[DiscountCondition]:
        result = await self.session.execute(select(DiscountCondition))
        return result.scalars().all()

    async def update(self, condition: DiscountCondition, data: dict) -> DiscountCondition:
        for key, value in data.items():
            setattr(condition, key, value)
        self.session.add(condition)
        await self.session.commit()
        await self.session.refresh(condition)
        return condition

    async def delete(self, condition: DiscountCondition):
        await self.session.delete(condition)
        await self.session.commit()
