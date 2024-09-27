document.getElementById('show').addEventListener('click', function() {
    let targetElement = document.querySelector('.form-container');
    let firstDiv = document.getElementById('div1');
    if (targetElement.style.display === 'block') {
        targetElement.style.display = 'none';
        firstDiv.style.textAlign = "center";
    } else {
        targetElement.style.display = 'block';
        firstDiv.style.textAlign = "left";   
    }
});
