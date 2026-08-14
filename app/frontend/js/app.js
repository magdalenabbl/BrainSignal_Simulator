let chart = null;

window.runSimulation = async function () {

    const model = document.getElementById("model").value.toLowerCase();
    const solver = document.getElementById("solver").value.toLowerCase();
    const T = Number(document.getElementById("T").value);
    const dt = Number(document.getElementById("dt").value);

    const response = await fetch("/simulation/run", {
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

    render(data);
};


function render(data) {

    if (chart) chart.destroy();

    const states = data.states || [];
    if (!states.length) return;

    const keys = new Set();

    states.forEach(s => {
        Object.keys(s || {}).forEach(k => keys.add(k));
    });

    const datasets = [...keys].map(key => {

        return {
            label: key,
            data: states.map(s => s?.[key] ?? 0),
            borderWidth: 2,
            pointRadius: 0,
            tension: 0.35
        };
    });

    chart = new Chart(document.getElementById("chart"), {
        type: "line",
        data: {
            labels: data.time || states.map((_, i) => i),
            datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: "#fff" }
                }
            },
            scales: {
                x: { ticks: { color: "#aaa" } },
                y: { ticks: { color: "#aaa" } }
            }
        }
    });

    renderInfo(data);
}


function renderInfo(data) {

    const container = document.getElementById("spikes");
    const last = data.states[data.states.length - 1];

    if (!last) {
        container.innerHTML = "No data";
        return;
    }

    let html = "<h3>Final state</h3>";

    for (const k in last) {
        html += `${k}: ${last[k]}<br>`;
    }

    container.innerHTML = html;
}