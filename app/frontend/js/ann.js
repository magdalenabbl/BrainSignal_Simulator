console.log("THIS IS MY NEW ANN.JS");
// Store the result of the last prediction
let lastPrediction = null;


// Store the training loss chart
let trainingChart = null;


// Train the ANN using an uploaded CSV file
window.trainANN = async function () {

    // Get the selected CSV file from the HTML input
    const fileInput = document.getElementById("dataset");

    const file = fileInput.files[0];


    // Check that a file was selected
    if (!file) {

        alert("Please select a CSV file.");

        return;
    }


    // FormData is used to send files through HTTP
    const formData = new FormData();


    // "file" must have the same name as the parameter
    // in ann_routes.py:
    //
    // async def train_ann(file: UploadFile = File(...))
    formData.append("file", file);


    // Send the CSV file to the API
    const response = await fetch("/ann/train", {

        method: "POST",

        body: formData

    });


    // Convert the API response from JSON
    const data = await response.json();

console.log("TRAIN RESPONSE:", data);
console.log("LOSS:", data.loss);
console.log("EPOCHS:", data.epochs);
console.log("ACCURACY:", data.accuracy);


    // Check if the request was successful
    if (!response.ok) {

        alert(data.detail || "Training failed.");

        return;
    }


    // Show the training result
    document.getElementById("trainStatus").textContent =
        data.message;


    // Update the network status
    document.getElementById("networkStatus").textContent =
        "Trained";


    // Display the training information
    // returned by ANNService.
    renderTrainingInfo(data);


    // Display the training loss graph.
    // renderTrainingChart(data.loss);
    if (Array.isArray(data.loss)) {

    renderTrainingChart(data.loss);

} else {

    console.log("No loss data received.");

}
};


// Display training information
function renderTrainingInfo(data) {

    // Find the training status element
    const container =
        document.getElementById("trainStatus");


    // Display the number of epochs and accuracy
    // together with the training message.
    container.textContent =
        `${data.message} | ` +
        `Epochs: ${data.epochs} | ` +
        `Accuracy: ${(data.accuracy * 100).toFixed(2)}%`;
}


// Display the training loss as a line chart
function renderTrainingChart(loss) {

    // Find the canvas used for the training chart
    const canvas =
        document.getElementById("trainingChart");


    // Stop if the canvas does not exist
    if (!canvas) {
        return;
    }


    // Destroy the previous chart
    if (trainingChart) {
        trainingChart.destroy();
    }


    // Create one label for every training epoch
    const labels = loss.map(
        (_, index) => index + 1
    );


    // Create the Chart.js line chart
    trainingChart = new Chart(
        canvas,
        {

            type: "line",

            data: {

                labels: labels,

                datasets: [
                    {
                        label: "Training Loss",

                        data: loss,

                        borderWidth: 2,

                        pointRadius: 0,

                        tension: 0.35
                    }
                ]
            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        labels: {
                            color: "#fff"
                        }
                    }
                },

                scales: {

                    x: {

                        title: {
                            display: true,
                            text: "Epoch",
                            color: "#aaa"
                        },

                        ticks: {
                            color: "#aaa"
                        }
                    },

                    y: {

                        title: {
                            display: true,
                            text: "Loss",
                            color: "#aaa"
                        },

                        ticks: {
                            color: "#aaa"
                        }
                    }
                }
            }
        }
    );
}


// Use the trained ANN to make a prediction
window.inferANN = async function () {

    // Read the two input values from the HTML
    const input1 = Number(
        document.getElementById("input1").value
    );

    const input2 = Number(
        document.getElementById("input2").value
    );


    // Send the input values to the API
    const response = await fetch("/ann/infer", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            inputs: [input1, input2]

        })

    });


    // Convert the API response to JavaScript object
    const data = await response.json();

    console.log("TRAIN RESPONSE:", data);

    // Check for an API error
    if (!response.ok) {

        alert(data.detail || "Inference failed.");

        return;
    }


    // Store the prediction
    lastPrediction = data.prediction;


    // Show the prediction in the interface
    document.getElementById("predictionValue").textContent =
        data.prediction;

};