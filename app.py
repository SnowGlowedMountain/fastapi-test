import fastapi, uvicorn
from starlette.requests import Request
import os

api = fastapi.FastAPI()

@api.get('/hello')
def hello(request: Request):
    return "Hello World!"

if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        api,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        log_level=os.getenv('LOG_LEVEL', "info")
    )