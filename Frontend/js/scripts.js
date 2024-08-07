document.getElementById('diabetes-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = parseFloat(value);
    });

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = 
            `Prediction: ${result.prediction}\nSuggestions: ${result.suggestions}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
