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
});
