from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from watchfiles import awatch

from ads_service.db.session import get_db
from ads_service.api.models import Ads_sc, Category_sc, Dormitory_sc, AdUpdate_sc
from ads_service.api.actions.ads import _create_new_ad, _create_new_category, _create_new_dormitory, _delete_dormitory, \
    _delete_ad, _delete_category, _update_ad

user_router = APIRouter()


@user_router.post("/", response_model=Ads_sc)
async def create_user(body: Ads_sc, db: AsyncSession = Depends(get_db)):
    return await _create_new_ad(body, db)


@user_router.post("/categories", response_model=Category_sc)
async def create_category(body: Category_sc, db: AsyncSession = Depends(get_db)):
    return await _create_new_category(body, db)


@user_router.post("/dormitories", response_model=Dormitory_sc)
async def create_dormitory(body: Dormitory_sc, db: AsyncSession = Depends(get_db)):
    return await _create_new_dormitory(body, db)


@user_router.delete("/dormitories/{dormitory_id}", status_code=204)
async def delete_dormitory(dormitory_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_dormitory(dormitory_id, db)


@user_router.delete("/categories/{category_id}", status_code=204)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_category(category_id, db)


@user_router.delete("/ads/{ad_id}", status_code=204)
async def delete_ad(ad_id: int, db: AsyncSession = Depends(get_db)):
    return await _delete_ad(ad_id, db)


@user_router.patch("/ads/{ad_id}", response_model=Ads_sc)
async def update_ad(ad_id: int, update: AdUpdate_sc = Body(...), db: AsyncSession = Depends(get_db)):
    return await _update_ad(ad_id, db, update)
