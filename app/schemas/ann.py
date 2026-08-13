from typing import List
from pydantic import BaseModel


# Data sent to /infer
class InferRequest(BaseModel):
    inputs: List[float]


# Response returned by /infer
class InferResponse(BaseModel):
    prediction: int


# Response returned after /train
class TrainResponse(BaseModel):
    message: str