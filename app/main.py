from fastapi import FastAPI

from app.api.simulation_routes import router as simulation_router

app = FastAPI(title="BrainSignal Simulator")

app.include_router(simulation_router)
@app.get("/")
def home():
    return {"message": "BrainSignal running"}