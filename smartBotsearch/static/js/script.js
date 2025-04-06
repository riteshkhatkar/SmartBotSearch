document.addEventListener('DOMContentLoaded', function() {
    // Search autocomplete
    const searchInput = document.getElementById('main-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.trim();
            if (query.length > 2) {
                fetch(`/api/tools?q=${encodeURIComponent(query)}`)
                    .then(response => response.json())
                    .then(data => {
                        // Show suggestions (you can implement a dropdown UI)
                        console.log('Suggestions:', data);
                    })
                    .catch(error => console.error('Error:', error));
            }
        });
    }

    // Category cards animation
    const categoryCards = document.querySelectorAll('.category-card');
    categoryCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.card').style.transform = 'scale(1.03)';
        });
        card.addEventListener('mouseleave', function() {
            this.querySelector('.card').style.transform = 'scale(1)';
        });
    });
});