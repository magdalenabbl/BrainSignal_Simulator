from fastapi import APIRouter
from app.schemas.ann import (TrainRequest, TrainResponse, InferRequest, InferResponse)
from app.services.ann_service import ANNService


# APIRouter is used to separate related API endpoints and other endpoints inside main.py,
router = APIRouter()
ann_service = ANNService()

# if HTTP POST request to this path - run train_ann()   POST /train -> train_ann()
# "/train" is the enpoint path, response_model=TrainResponse tells FastAPI what format the response should have

@router.post("/train", response_model=TrainResponse)
def train_ann(request: TrainRequest):

    # FastAPI automatically converts the incoming JSON into a TrainRequest object 
    # The endpoint does not train the network, only passes the request data to the service
    result = ann_service.train(
        data=request.data,
        epochs=request.epochs
    )

    # Return the result to FastAPI
    return result


@router.post("/infer", response_model=InferResponse)
def infer_ann(request: InferRequest):

    # Call the service instead of using ANN directly to keeps the API layer separate from the ANN business logic.
    result = ann_service.infer(
        inputs=request.inputs
    )

    return result