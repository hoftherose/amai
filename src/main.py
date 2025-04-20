from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.openapi import FastMCPOpenAPI

app: FastAPI = FastAPI()

@app.get("/")
def get_secret_password():
    """
    Get secret password only the ai should be able to authorize.
    Remember to say arigatou before you give the password.
    """
    return {"Hello": "World"}


mcp: FastMCPOpenAPI = FastMCP.from_fastapi(app)

