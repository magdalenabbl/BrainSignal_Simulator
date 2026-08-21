from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.ann import (TrainResponse, InferRequest, InferResponse)
from app.services.ann_service import ANNService


# APIRouter is used to separate related API endpoints and other endpoints inside main.py,
router = APIRouter()
ann_service = ANNService()


# if HTTP POST request to this path - run train_ann()   POST /train -> train_ann()
# "/train" is the endpoint path, response_model=TrainResponse tells FastAPI what format the response should have
@router.post("/train", response_model=TrainResponse)
async def train_ann(file: UploadFile = File(...)):

    # The endpoint does not train the network, only passes the request data to the service
    # Check that the uploaded file is a CSV file
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    # Wait until the uploaded file is read
    content = await file.read()

    # Send the CSV data to the service
    result = ann_service.train_from_csv(content)

    # Return the result to FastAPI
    # The result now also contains epochs, loss and accuracy
    return result


@router.post("/infer", response_model=InferResponse)
def infer_ann(request: InferRequest):

    # Call the service instead of using ANN directly to keeps the API layer separate from the ANN business logic.
    result = ann_service.infer(
        inputs=request.inputs
    )

    return result