function addFormset(prefix, containerId, formCountId) {
    let container = document.getElementById(containerId);
    // Ensure the template exists
    let template = container.querySelector('.form-template');
    
    if (!template) {
        console.error('Template not found');
        return;  // Stop execution if the template is not found
    }

    let totalForms = document.querySelector(`#${containerId} input[name="${prefix}-TOTAL_FORMS"]`);
    let newForm = template.cloneNode(true);
    let formRegex = new RegExp(`__prefix__`, 'g');
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, totalForms.value);
    newForm.classList.remove('form-template');
    newForm.style.display = 'block';
    container.appendChild(newForm);
    totalForms.value = parseInt(totalForms.value) + 1;
}


document.getElementById('add-project').addEventListener('click', function() {
    addFormset('projects', 'project-formset', 'id_projects-TOTAL_FORMS');
});

document.getElementById('add-link').addEventListener('click', function() {
    addFormset('links', 'link-formset', 'id_links-TOTAL_FORMS');
});

document.getElementById('add-image').addEventListener('click', function() {
    addFormset('images', 'image-formset', 'id_images-TOTAL_FORMS');
});