let chart = null;

window.runSimulation = async function () {

    const model = document.getElementById("model").value;
    const solver = document.getElementById("solver").value;
    const T = parseFloat(document.getElementById("T").value);
    const dt = parseFloat(document.getElementById("dt").value);

    const response = await fetch("http://127.0.0.1:8000/simulation/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            model,
            solver,
            T,
            dt,
            params: {}
        })
    });

    const data = await response.json();

    drawChart(data.time, data.states);
    drawSpikes(data.states);
}
function drawChart(time, states) {

    const x = states.map(s => s.x);

    const ctx = document.getElementById("chart");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: time,
            datasets: [{
                label: "x(t)",
                data: x,
                borderColor: "blue",
                fill: false
            }]
        }
    });
}

function drawSpikes(states) {

    const container = document.getElementById("spikes");
    container.innerHTML = "";

    const last = states[states.length - 1];

    if (!last || last.V === undefined) {
        container.innerHTML = "No spike data (use SNN/LIF model)";
        return;
    }

    container.innerHTML = `
        <div>Membrane potential: ${last.V.toFixed(2)}</div>
    `;
}