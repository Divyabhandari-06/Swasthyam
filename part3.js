// script.js
function updateHealthProfile() {
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const pulse = document.getElementById('pulse').value;
    const bloodPressure = document.getElementById('blood-pressure').value;
    const stressLevel = document.getElementById('stress-level').value;

    const profile = `Weight: ${weight} kg, Height: ${height} cm, Pulse: ${pulse} bpm, Blood Pressure: ${bloodPressure}, Stress: ${stressLevel}`;
    document.getElementById('health-profile-display').textContent = profile;
}

function generateCustomPlan() {
    // Simulated AI customization
    document.getElementById('custom-plan-display').textContent = "Personalized Yoga and Diet plan generated based on your profile.";
}

function startMeditation() {
    // Simulated meditation
    document.getElementById('meditation-display').textContent = "Starting guided meditation... (Simulated)";
}

function sendMessage() {
    const message = document.getElementById('chat-input').value;
    const chatContainer = document.getElementById('chat-container');
    chatContainer.innerHTML += `<p>You: ${message}</p>`;
    document.getElementById('chat-input').value = '';
    chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to bottom
    //Simulated reply
    setTimeout(()=> {
        chatContainer.innerHTML += `<p>Swasthyam Bot: Great job!</p>`;
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }, 1000);
}