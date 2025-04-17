import uvicorn
from fastapi import FastAPI, APIRouter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ads_service import settings
from ads_service.api.handlers import user_router
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

app = FastAPI()
main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/ads", tags=["ads"])
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 8001)