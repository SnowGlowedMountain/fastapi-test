import fastapi, uvicorn
import os

app = fastapi.FastAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(app, port=8080, host='0.0.0.0')
