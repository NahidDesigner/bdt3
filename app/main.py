from fastapi import FastAPI

from app.middleware import resolve_tenant
from app.routers import health

app = FastAPI()

app.middleware("http")(resolve_tenant)

app.include_router(health.router)

