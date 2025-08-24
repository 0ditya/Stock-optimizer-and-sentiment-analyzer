document.getElementById('stockForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var stockSymbol = document.getElementById('stockSymbol').value; // Get the value from the input field
    var apiUrl = `http://localhost:5000/analyze?symbols=${stockSymbol}`; // Prepare the API URL

    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // process data
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to fetch data. Check console for details.');
    });

});

function updateUI(weights) {
    const resultsContainer = document.getElementById('results'); // Assuming there is a div with id='results'
    resultsContainer.innerHTML = `<h3>Optimized Weights:</h3><p>${weights.join(', ')}</p>`; // Display weights
}
