from app.neural.ann import ANN
import csv
import io


# API -> ANNService -> ANN

class ANNService:

    def __init__(self):
        self.ann = ANN()

    def train_from_csv(self, content: bytes):

        # Convert file bytes to text
        text = content.decode("utf-8")

        # Read rows from the CSV file; dictionary
        reader = csv.DictReader(
            io.StringIO(text)  # text to file
        )

        training_data = []

        for row in reader:

            # Read the two input values
            inputs = [
                float(row["input_1"]),
                float(row["input_2"])
            ]

            # Read the expected output
            target = int(row["target"])

            # dictionary -> tuple ([0.0, 1.0], 1)
            # [input_1, input_2], target

            # Store data in the format expected by ANN.train()
            training_data.append(
                (inputs, target)
            )

        # Train the neural network
        epochs = 5000

        self.ann.train(
            training_data,
            epochs=epochs
        )

        # Return training result to API
        return {
            "message": "Training completed",

            # Return the number of epochs used
            # so the frontend can display it.
            "epochs": epochs,

            # Return the loss recorded during training
            # so the frontend can create a loss graph.
            "loss": self.ann.loss_history,

            # Return the final accuracy of the network
            # so the frontend can display the result.
            "accuracy": self.ann.accuracy
        }

    # Use the already trained network like [0, 1]
    def infer(self, inputs):

        # The same ANN object
        prediction = self.ann.predict(inputs)

        # Return prediction to API
        return {
            "prediction": prediction
        }