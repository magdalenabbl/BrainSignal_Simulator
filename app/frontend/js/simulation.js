// Store the current chart
let simulationChart = null;


// Run a simulation
window.runSimulation = async function () {

    // Read the selected model from the HTML
    const model = document
        .getElementById("model")
        .value
        .toLowerCase();


    // Read the selected solver from the HTML
    const solver = document
        .getElementById("solver")
        .value
        .toLowerCase();


    // Read the total simulation time
    const T = Number(
        document.getElementById("T").value
    );


    // Read the time step
    const dt = Number(
        document.getElementById("dt").value
    );


    // Prepare the data that will be sent to FastAPI
    const requestData = {
        model: model,
        solver: solver,
        T: T,
        dt: dt,
        params: {}
    };


    try {

        // Send an HTTP POST request to the simulation endpoint
        const response = await fetch("/simulation/run", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(requestData)
        });


        // Convert the HTTP response from JSON
        const data = await response.json();


        // Check if FastAPI returned an error
        if (!response.ok) {

            alert(
                data.detail ||
                "Simulation failed."
            );

            return;
        }


        // Display the simulation result
        renderSimulation(data);


    } catch (error) {

        // Handle connection or network errors
        console.error(
            "Simulation request failed:",
            error
        );

        alert(
            "Could not connect to the simulation API."
        );
    }
};



// Render simulation data
function renderSimulation(data) {

    // Destroy the previous chart
    if (simulationChart) {
        simulationChart.destroy();
    }


    // Get simulation states
    const states = data.states || [];


    // Stop if there is no simulation data
    if (!states.length) {
        return;
    }


    // Find all variables contained in the states
    const keys = new Set();


    states.forEach(state => {

        Object.keys(state || {}).forEach(key => {

            keys.add(key);

        });

    });


    // Create one Chart.js dataset for every state variable
    const datasets = [...keys].map(key => {

        return {

            // Name shown in the chart legend
            label: key,

            // Values for this variable
            data: states.map(
                state => state?.[key] ?? 0
            ),

            borderWidth: 2,

            // Do not display a point for every value
            pointRadius: 0,

            // Make the line smoother
            tension: 0.35
        };
    });


    // Create the chart
    simulationChart = new Chart(
        document.getElementById("chart"),
        {

            type: "line",

            data: {

                // X-axis
                labels:
                    data.time ||
                    states.map((_, index) => index),

                // Y-axis datasets
                datasets: datasets
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

                        ticks: {
                            color: "#aaa"
                        }
                    },


                    y: {

                        ticks: {
                            color: "#aaa"
                        }
                    }
                }
            }
        }
    );


    // Display information about the final state
    renderSimulationInfo(data);
};



// Display the final simulation state
function renderSimulationInfo(data) {

    // Find the information container
    const container =
        document.getElementById("spikes");


    // Get the last state
    const states = data.states || [];

    const last =
        states[states.length - 1];


    // If there is no final state
    if (!last) {

        container.innerHTML =
            "No data";

        return;
    }


    // Create the information HTML
    let html = "<h3>Final state</h3>";


    // Add every variable from the final state
    for (const key in last) {

        html +=
            `${key}: ${last[key]}<br>`;
    }


    // Display the information
    container.innerHTML = html;
}