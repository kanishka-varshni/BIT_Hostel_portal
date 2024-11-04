document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const room = document.getElementById('room').value;
    const date = document.getElementById('date').value;

    alert(`Room ${room} booked for ${name} on ${date}`);
});
