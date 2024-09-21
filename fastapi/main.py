from fastapi import FastAPI
from settings import add_cors_middleware

app = FastAPI()

# add_cors_middleware(app)

@app.get('/')
async def home() -> dict:
    return {'message': 'Welcome to the CodeScript API'}

# uvicorn main:app --host 0.0.0.0 --port 80
