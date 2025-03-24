document.getElementById('healthForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    alert(Your weight: ${weight}kg, height: ${height}cm);
});
