document.querySelectorAll('.project-title').forEach(title => {
    title.addEventListener('click', () => {
        const details = title.nextElementSibling;
        if (details.style.display === 'block') {
            details.style.display = 'none';
        } else {
            details.style.display = 'block';
        }
    });
});

document.getElementById('like-form').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch(this.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': this.querySelector('[name=csrfmiddlewaretoken]').value,
        },
    })
    .then(response => {
        // Check if response is ok and JSON, otherwise handle error
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text) });
        }
        return response.json(); // Ensure the response is JSON
    })
    .then(data => {
        document.getElementById('like-count').textContent = data.likes_count;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
