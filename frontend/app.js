document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const storyText = document.getElementById("storyInput").value;
    if (!storyText.trim()) {
        alert("Please paste some text before analyzing.");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/analyze-story", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: storyText })
    });

    if (!response.ok) {
        alert("Error contacting backend. Is FastAPI running?");
        return;
    }

    const data = await response.json();
    console.log("DEBUG:", data);
    const tableBody = document.querySelector("#resultsTable tbody");
    tableBody.innerHTML = "";

    document.getElementById("povValue").textContent = data.pov;
    data.characters.forEach(char => {
        const row = document.createElement("tr");
        const nameCell = document.createElement("td");
        const genderCell = document.createElement("td");

        nameCell.textContent = char.name;
        genderCell.textContent = char.gender;

        row.appendChild(nameCell);
        row.appendChild(genderCell);
        tableBody.appendChild(row);
    });

    // Build nodes and edges for network
    const nodes = data.graph?.nodes || [];
    const edges = data.graph?.edges || [];

    // Build vis.js data structure
    const visNodes = nodes.map(n => ({ id: n.id, label: n.id }));
    const visEdges = edges.map(e => ({ from: e.from, to: e.to, value: e.value }));

    const container = document.getElementById("network");
    const networkData = { nodes: new vis.DataSet(visNodes), edges: new vis.DataSet(visEdges) };
    const options = { edges: { arrows: "to", smooth: true }, nodes: { shape: "dot", size: 20 } };

    new vis.Network(container, networkData, options);

});
