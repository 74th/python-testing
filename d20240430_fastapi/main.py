from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    group: int

class ErrorResponseEception(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

@app.exception_handler(ErrorResponseEception)
async def error_response_exception_handler(request:Request, exc: ErrorResponseEception):
    return JSONResponse(
        status_code=200,
        content={
            "success": False,
            "code": exc.code,
            "message": exc.message},
    )

@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(request:Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=200,
        content={
            "success": False,
            "code": 40000,
            "message": "validation error",
            "detail": exc.errors()},
    )

@app.post("/user")
async def post_user(user: User):
    print(user)
    return {"message": "Hello World"}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    if user_id == 1000:
        raise ErrorResponseEception(code=40000, message="User not found")
    return User(id=user_id, group=100)
