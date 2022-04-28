import fastapi
from fastapi import responses
from fastapi.middleware.cors import CORSMiddleware


def register_features(app: fastapi.FastAPI) -> None:
    from src.features import order
    router = fastapi.APIRouter()
    router.include_router(order.router)
    app.include_router(router)


def make_asgi_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    origins = [
        "http://localhost:3000",
        "http://localhost:8080",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_features(app)
    return app
