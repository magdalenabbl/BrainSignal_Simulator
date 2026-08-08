from app.neural.ann import ANN

# API->ANNService -> ANN

class ANNService:

    def __init__(self):
        self.ann = ANN()

    def train(self, data, epochs):

        # Convert Pydantic objects (TrainingExample from schemas/ann) to ANN training format
        training_data = [
            (example.inputs, example.target)
            for example in data
        ]

        # Train the neural network using ANN
        self.ann.train(
            training_data,
            epochs=epochs
        )

        # Return training result to API
        return {
            "message": "Training completed"
        }
    
    # using the trained network with new input data
    def infer(self, inputs):

        prediction = self.ann.predict(inputs)

        # Return prediction to the API
        return {
            "prediction": prediction
        }