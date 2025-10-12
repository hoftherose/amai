from fastapi import APIRouter

health_router = APIRouter(prefix="/healthz")


@health_router.get("")
def health():
    return {"status": "up"}
