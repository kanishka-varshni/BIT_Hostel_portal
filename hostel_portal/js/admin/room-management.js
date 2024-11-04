document.addEventListener('DOMContentLoaded', function() {
    const roomList = document.getElementById('roomList');

    const rooms = [
        { number: '101', capacity: 2, occupancy: 1 },
        { number: '102', capacity: 3, occupancy: 2 }
    ];

    let roomsHTML = '<ul>';
    rooms.forEach(room => {
        roomsHTML += `<li>Room ${room.number} - Capacity: ${room.capacity}, Occupancy: ${room.occupancy}</li>`;
    });
    roomsHTML += '</ul>';

    roomList.innerHTML = roomsHTML;
});
