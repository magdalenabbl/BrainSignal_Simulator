// Store the result of the last prediction
let lastPrediction = null;


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

};


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