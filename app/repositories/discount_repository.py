from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.discount import Discount

class DiscountRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> Discount:
        discount = Discount(**data)
        self.session.add(discount)
        await self.session.commit()
        await self.session.refresh(discount)
        return discount

    async def get_by_id(self, id: int) -> Discount | None:
        return await self.session.get(Discount, id)

    async def get_by_code(self, code: str) -> Discount | None:
        result = await self.session.execute(
            select(Discount).where(Discount.code == code)
        )
        return result.scalar_one_or_none()

    async def list(self) -> list[Discount]:
        result = await self.session.execute(select(Discount))
        return result.scalars().all()

    async def update(self, discount: Discount, data: dict) -> Discount:
        for key, value in data.items():
            setattr(discount, key, value)
        self.session.add(discount)
        await self.session.commit()
        await self.session.refresh(discount)
        return discount

    async def delete(self, discount: Discount):
        await self.session.delete(discount)
        await self.session.commit()
