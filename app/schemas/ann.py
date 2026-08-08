from typing import List
from pydantic import BaseModel


class TrainingExample(BaseModel):
    inputs: List[float] # "inputs": [0, 1]
    target: int # "target": 1


class TrainRequest(BaseModel):
    data: List[TrainingExample]
    epochs: int = 5000 # default


class TrainResponse(BaseModel):
    message: str

# after the training
class InferRequest(BaseModel):
    inputs: List[float]


class InferResponse(BaseModel):
    prediction: int