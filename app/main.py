from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.models.base import Base
from core.config import settings
from core.models.db_helper import db_helper
from core.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
