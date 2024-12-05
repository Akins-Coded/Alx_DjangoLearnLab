// Basic example script to demonstrate dynamic behavior
document.addEventListener('DOMContentLoaded', function () {
    console.log('Blog page loaded');

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                    displayError(input, 'This field is required');
                } else {
                    input.classList.remove('error');
                    clearError(input);
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    });

    // Handle delete confirmation
    const deleteButtons = document.querySelectorAll('.button.delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Highlight active links
    const links = document.querySelectorAll('a');
    const currentPath = window.location.pathname;

    links.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Add character count for text areas
    const textAreas = document.querySelectorAll('textarea');
    textAreas.forEach(textArea => {
        const counter = document.createElement('small');
        counter.className = 'char-counter';
        counter.textContent = `0/${textArea.maxLength || 500} characters`;
        textArea.parentNode.insertBefore(counter, textArea.nextSibling);

        textArea.addEventListener('input', () => {
            counter.textContent = `${textArea.value.length}/${textArea.maxLength || 500} characters`;
        });
    });

    // Display dynamic greeting in the profile page (Check if the element exists first)
    const profileGreeting = document.querySelector('.profile-container h2');
    if (profileGreeting) {
        const usernameInput = document.querySelector('#username');
        const username = usernameInput ? usernameInput.value : 'User';
        profileGreeting.textContent = `Welcome, ${username}!`;
    }
});

// Utility functions
function displayError(input, message) {
    let errorElement = input.parentNode.querySelector('.error-message');
    if (!errorElement) {
        errorElement = document.createElement('small');
        errorElement.className = 'error-message';
        input.parentNode.appendChild(errorElement);
    }
    errorElement.textContent = message;
}

function clearError(input) {
    const errorElement = input.parentNode.querySelector('.error-message');
    if (errorElement) {
        input.parentNode.removeChild(errorElement);
    }
}
