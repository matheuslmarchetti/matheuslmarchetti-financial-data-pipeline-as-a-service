from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.v1.router import api_router
from app.pipeline.scheduler import run_daily_simulation


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    run_daily_simulation()
    yield
    # Shutdown (se precisar no futuro)


app = FastAPI(
    title="Financial Data Pipeline API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api/v1")