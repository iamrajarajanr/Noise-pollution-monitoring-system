// Function to fetch and display real-time noise data
function fetchNoiseData() {
    // Replace this with actual data retrieval from your IoT sensors or API
    const noiseData = {
        sensor1: 75.5,
        sensor2: 68.2,
        sensor3: 71.8,
    };

    const noiseDataDiv = document.getElementById('noise-data');
    noiseDataDiv.innerHTML = '<h2>Noise Level Data</h2>';
    
    for (const sensor in noiseData) {
        const noiseLevel = noiseData[sensor];
        const sensorDiv = document.createElement('div');
        sensorDiv.innerHTML = `<p>${sensor}: ${noiseLevel} dB</p>`;
        noiseDataDiv.appendChild(sensorDiv);
    }
}

// Fetch and display data every 5 seconds (adjust as needed)
setInterval(fetchNoiseData, 5000);
fetchNoiseData(); // Fetch data initially
