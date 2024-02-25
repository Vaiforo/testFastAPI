from fastapi import FastAPI
from functools import cache
import uvicorn


@cache
def app_factory() -> FastAPI:
    app = FastAPI()

    @app.get('/')
    def root() -> str:
        return "Hello, FastAPI!"

    @app.get("/tasks")
    def list_tasks():
        return [
            {
                "id": 123,
                "title": "Test",
                "description": "description test"
            }
        ]

    return app


if __name__ == '__main__':
    uvicorn.run(
        'src.main:app_factory',
        host="127.0.0.1",
        port=5000,
        reload=True,
    )
