from fastapi import FastAPI
from meshy import Meshy

app = FastAPI()
meshy = Meshy()

@app.get("/")
async def home():
    return({'Data': 'Test'})

@app.post("/sample")
async def sample():
    meshy.sample()
