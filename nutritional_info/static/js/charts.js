// Get the canvas element by its ID
const ctx = document.getElementById('myPieChart').getContext('2d');

var protein = parseFloat(document.getElementById('protein').textContent);
var carbo = parseFloat(document.getElementById('carbo').textContent);
var fat = parseFloat(document.getElementById('fat').textContent);

// Data for the pie chart
const data = {
    labels: ['Proteínas', 'Carboidratos', 'Gordura'],
    datasets: [{
        data: [protein, carbo, fat], // Values for each item
        backgroundColor: ['#20C389', '#C3F3E0', '#DFF4EB'], // Colors for each item
    }]
};

// Configuration options for the pie chart
const options = {
    responsive: true,
    maintainAspectRatio: false,
};

// Create a new pie chart instance
const myPieChart = new Chart(ctx, {
    type: 'pie',
    data: data,
    options: options
});
