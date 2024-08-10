import logging
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.db.dependencies import db_helper
from src.logging_conf import setup_logger
from src.settings import settings

APP_ROOT = Path(__file__).parent
setup_logger()

logger = logging.getLogger('fastapi_app')


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


def mount_folders(app: FastAPI):
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )
    app.mount("/media", StaticFiles(directory=APP_ROOT / "media"), name="media")


def create_app() -> FastAPI:
    logger.debug("Creating app...")
    app = FastAPI(
        title="Telegram Marketplace Bot API",
        version="1.0.0",
        default_response_class=ORJSONResponse,
        lifespan=lifespan
    )

    logger.debug("Mount folders...")
    mount_folders(app)

    logger.debug("Configure middleware...")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
