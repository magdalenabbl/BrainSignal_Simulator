from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.routes import api_router
import os


app = FastAPI(
    title="BrainSignal Simulator",
    description="Numerical simulation platform for biological and dynamical systems.",
    version="1.0.0"
)

app.include_router(api_router)

# Makes the files inside app/frontend (HTML, CSS and JavaScript) accessible through FastAPI.
app.mount(
    "/static",
    StaticFiles(directory="app/frontend"),
    name="static"
)

# When opening the link FastAPI returns index.html.
@app.get("/")
def root():
    print("LOADING FILE FROM:", os.path.abspath("app/frontend/index.html"))
    return FileResponse("app/frontend/index.html")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)