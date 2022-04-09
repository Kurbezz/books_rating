from fastapi import FastAPI

from prometheus_fastapi_instrumentator import Instrumentator

from app.views import router, healtcheck_router
from core.db import database


def start_app() -> FastAPI:
    app = FastAPI()

    app.state.database = database

    app.include_router(router)
    app.include_router(healtcheck_router)

    @app.on_event("startup")
    async def startup() -> None:
        database_ = app.state.database
        if not database_.is_connected:
            await database_.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        database_ = app.state.database
        if database_.is_connected:
            await database_.disconnect()

    Instrumentator().instrument(app).expose(app, include_in_schema=True)

    return app