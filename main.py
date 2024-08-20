from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(app, port=8080, host='0.0.0.0')