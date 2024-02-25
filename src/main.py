from fastapi import FastAPI
from functools import cache
import uvicorn
from src.tasks.routes import router


@cache
def app_factory() -> FastAPI:
    app = FastAPI()

    app.include_router(router)

    return app


if __name__ == '__main__':
    uvicorn.run(
        'src.main:app_factory',
        host="127.0.0.1",
        port=5000,
        reload=True,
    )
