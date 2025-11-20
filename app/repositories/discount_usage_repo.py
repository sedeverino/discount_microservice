from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.discount_usage import DiscountUsage

class DiscountUsageRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> DiscountUsage:
        usage = DiscountUsage(**data)
        self.session.add(usage)
        await self.session.commit()
        await self.session.refresh(usage)
        return usage

    async def get_by_id(self, id: int) -> DiscountUsage | None:
        return await self.session.get(DiscountUsage, id)

    async def get_by_user(self, user_id: int) -> list[DiscountUsage]:
        result = await self.session.execute(
            select(DiscountUsage).where(DiscountUsage.user_id == user_id)
        )
        return result.scalars().all()

    async def get_by_discount_id(self, discount_id: int) -> list[DiscountUsage]:
        result = await self.session.execute(
            select(DiscountUsage).where(DiscountUsage.discount_id == discount_id)
        )
        return result.scalars().all()

    async def list(self) -> list[DiscountUsage]:
        result = await self.session.execute(select(DiscountUsage))
        return result.scalars().all()

    async def delete(self, usage: DiscountUsage):
        await self.session.delete(usage)
        await self.session.commit()
