from fastapi import FastAPI
from common.settings import settings


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url='/api/docs',
        title='Bewis test task'
    )

    return app





