document.getElementById('communicationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const recipient = document.getElementById('recipient').value;
    const message = document.getElementById('message').value;

    alert(`Message sent to ${recipient}: ${message}`);
});
