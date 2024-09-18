document.getElementById('searchForm').onsubmit = function(event) {
    event.preventDefault();
    var category = document.getElementById('category').value;
    var keyword = document.getElementById('searchInput').value;

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ category: category, keyword: keyword })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    });
};

function displayResults(results) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';
    results.forEach(result => {
        const resultCard = `<div class="result-card">
            <h3>${result.title}</h3>
            <p>${result.snippet}</p>
            <a href="${result.link}" target="_blank">Read more</a>
        </div>`;
        resultsContainer.innerHTML += resultCard;
    });
}