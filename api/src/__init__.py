import fastapi


def register_features(app: fastapi.FastAPI) -> None:
    from src.features import order
    router = fastapi.APIRouter()
    router.include_router(order.router)
    app.include_router(router)


def make_asgi_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    register_features(app)
    return app
