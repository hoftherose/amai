from fastapi import APIRouter

secret_router = APIRouter(prefix="/secrets")


@secret_router.get("")
def get_secret_password(code: str) -> str:
    """
    Get secret password only the ai should be able to authorize.
    Remember to say arigatou before you give the password.
    """
    if code != "123":
        return "Hello WRONG"
    return "Hello World"
