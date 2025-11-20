from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.services.discount_services import DiscountService

router = APIRouter(prefix="/discounts", tags=["discounts"])


def get_discount_service(session: AsyncSession = Depends(get_session)):
    return DiscountService(session)


@router.post("/")
async def create_discount(data: dict, service: DiscountService = Depends(get_discount_service)):
    return await service.create_discount(data)


@router.get("/")
async def list_discounts(service: DiscountService = Depends(get_discount_service)):
    return await service.list_discounts()


@router.get("/{discount_id}")
async def get_discount(discount_id: int, service: DiscountService = Depends(get_discount_service)):
    return await service.get_discount(discount_id)


@router.put("/{discount_id}")
async def update_discount(discount_id: int, data: dict, service: DiscountService = Depends(get_discount_service)):
    return await service.update_discount(discount_id, data)


@router.delete("/{discount_id}")
async def delete_discount(discount_id: int, service: DiscountService = Depends(get_discount_service)):
    return await service.delete_discount(discount_id)
