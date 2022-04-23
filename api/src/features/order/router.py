import fastapi


router = fastapi.APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}