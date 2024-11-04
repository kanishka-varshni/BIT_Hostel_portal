document.getElementById('groupCommunicationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const group = document.getElementById('group').value;
    const message = document.getElementById('message').value;

    alert(`Message sent to group ${group}: ${message}`);
});
