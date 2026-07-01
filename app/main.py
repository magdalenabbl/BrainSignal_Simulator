from fastapi import FastAPI

from app.api.routes import api_router


app = FastAPI(
    title="BrainSignal Simulator",
    description="Numerical simulation platform for biological and dynamical systems.",
    version="1.0.0"
)


app.include_router(
    api_router
)


@app.get("/")
def root():
    """
    Health check endpoint.
    """

    return {
        "status": "running",
        "service": "BrainSignal Simulator"
    }