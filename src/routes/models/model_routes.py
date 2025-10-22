from fastapi import APIRouter

from src.models.base import Model


def generate_model_router(model: Model) -> APIRouter:
    temp_router = APIRouter(prefix=f"/{model.name}")
    def chat():
        return {"status": "success"}
    temp_router.add_api_route("/models", chat, methods=["POST"])
    return temp_router
