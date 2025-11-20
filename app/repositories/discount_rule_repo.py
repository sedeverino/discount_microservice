from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.discount_rule import DiscountRule

class DiscountRuleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> DiscountRule:
        rule = DiscountRule(**data)
        self.session.add(rule)
        await self.session.commit()
        await self.session.refresh(rule)
        return rule

    async def get_by_id(self, id: int) -> DiscountRule | None:
        return await self.session.get(DiscountRule, id)

    async def get_by_discount_id(self, discount_id: int) -> list[DiscountRule]:
        result = await self.session.execute(
            select(DiscountRule).where(DiscountRule.discount_id == discount_id)
        )
        return result.scalars().all()

    async def increment_usage(self, rule: DiscountRule):
        rule.uses_count += 1
        self.session.add(rule)
        await self.session.commit()

    async def list(self) -> list[DiscountRule]:
        result = await self.session.execute(select(DiscountRule))
        return result.scalars().all()

    async def update(self, rule: DiscountRule, data: dict) -> DiscountRule:
        for key, value in data.items():
            setattr(rule, key, value)
        self.session.add(rule)
        await self.session.commit()
        await self.session.refresh(rule)
        return rule

    async def delete(self, rule: DiscountRule):
        await self.session.delete(rule)
        await self.session.commit()
