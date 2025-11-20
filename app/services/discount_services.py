from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.discount_repository import DiscountRepository
from app.models.discount import Discount

class DiscountService:
    def __init__(self, session: AsyncSession):
        self.repository = DiscountRepository(session)
        
    async def create_discount(self, data: dict) -> Discount:
        # Validar que el código no exista
        existing = await self.repository.get_by_code(data["code"])
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Discount code already exists."
            )

        return await self.repository.create(data)

    async def get_discount(self, discount_id: int) -> Discount:
        discount = await self.repository.get_by_id(discount_id)
        if not discount:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Discount not found."
            )
        return discount

    async def list_discounts(self) -> list[Discount]:
        return await self.repository.list()

    async def update_discount(self, discount_id: int, data: dict) -> Discount:
        discount = await self.repository.get_by_id(discount_id)
        if not discount:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Discount not found."
            )

        # Si el usuario envía un nuevo código, validar unicidad
        if "code" in data and data["code"] != discount.code:
            existing = await self.repository.get_by_code(data["code"])
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Another discount already uses this code."
                )

        return await self.repository.update(discount, data)

    async def delete_discount(self, discount_id: int):
        discount = await self.repository.get_by_id(discount_id)
        if not discount:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Discount not found."
            )

        await self.repository.delete(discount)
        return {"message": "Discount deleted successfully."}
