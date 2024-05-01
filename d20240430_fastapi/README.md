# fastapi のお試し

ノリは Flask と変わらない

```py
from fastapi import FastAPI
app = FastAPI()
```

## 入力する RequestBody の JSON の検証

pydantic の BaseModel を使うことでやってくれる。

```py
class User(BaseModel):
    id: int
    group: int

@app.post("/user")
async def post_user(user: User):
    print(user)
    return {"message": "Hello World"}
```

## カスタムエラーレスポンス

`@app.exception_handler(ErrorResponseEception)` でラップしたハンドラーを作る

```py
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
```

## pydantic の BaseModel エラーのバリデーションをでカスタムエラーレスポンスを返す

`fastapi.exceptions.RequestValidationError`というのが上がるので、それを同様にハンドリングする

```py
from fastapi.exceptions import RequestValidationError

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
```
