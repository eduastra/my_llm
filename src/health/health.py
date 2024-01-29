from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


health_router = APIRouter()


@health_router.get("/liveness")
async def liveness(Request: Request) -> JSONResponse:
    try:
        return JSONResponse(content={"detail":  "Server is running, and alive"}, status_code=200)
    except:
        #TODO : Implement great menssagem
        pass


@health_router.get("/readiness")
async def readiness (Request: Request) -> JSONResponse:
    try:
        return JSONResponse(content="Server is ready to receive requests",status_code=200)
    except:
        #TODO : Implement great menssagem
        pass