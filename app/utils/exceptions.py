from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from http import HTTPStatus

class APIException(Exception):
    def __init__(self, status_code: int, reason : str = "", message: str = "", headers: dict[str, str] | None = None, **kwargs) -> None:
        if not reason: reason = HTTPStatus(status_code).phrase
        self.reason = reason
        self.message = message
        self.status_code = status_code
        self.headers = headers
        self.data = {
            "reason": reason,
            "message": message,
            **kwargs
        }

    def __str__(self) -> str:
        return f"{self.status_code}: {self.data}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, reason={self.reason!r}, message={self.message!r})"

def setup_exception_handlers(app: FastAPI):

    @app.exception_handler(APIException)    
    async def api_exception_handler(request: Request, exc: APIException):
        return JSONResponse(status_code=exc.status_code, content=jsonable_encoder(exc.data))

    @app.exception_handler(Exception)
    async def internal_exception_handler(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content=jsonable_encoder(
            {"reason": "Internal Server Error", "message": "An unexpected error occurred.",
            "details": {"exception": exc.__class__.__name__, "message": str(exc)}}
        ))