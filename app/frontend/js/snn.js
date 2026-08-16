// Store the current SNN result
let snnResult = null;


// Run the SNN simulation
window.runSNN = async function () {

    // Read values from the HTML form
    const input = Number(
        document.getElementById("snnInput").value
    );

    const steps = Number(
        document.getElementById("snnSteps").value
    );


    // Prepare the data that will be sent to the API
    const requestData = {
        input: input,
        steps: steps
    };


    try {

        // Send the request to the SNN API
        const response = await fetch("/snn/run", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        });


        // Convert the response to a JavaScript object
        const data = await response.json();


        // Check if the API returned an error
        if (!response.ok) {
            alert(data.detail || "SNN simulation failed.");
            return;
        }


        // Store the result
        snnResult = data;


        // Display the result
        renderSNN(data);

    } catch (error) {

        // Handle network or connection errors
        console.error("SNN request failed:", error);

        alert("Could not connect to the SNN API.");
    }
};


// Render the SNN result
function renderSNN(data) {

    // Get the result container
    const container =
        document.getElementById("snnResult");


    // Clear previous result
    container.innerHTML = "";


    // Display the result
    container.innerHTML = `
        <h3>SNN Result</h3>
        <p>Output: ${data.output ?? "No output"}</p>
    `;
}