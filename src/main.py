from fastapi import FastAPI
from db.core.config.settings import settings

app = FastAPI(title="Task Tracker", description='Лучший в мире Task Tracker', version='beta-test-0.1')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        reload=settings.FASTAPI_RELOAD,
        port=settings.FASTAPI_PORT,
        host=settings.FASTAPI_HOST
    )

