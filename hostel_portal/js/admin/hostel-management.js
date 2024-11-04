document.addEventListener('DOMContentLoaded', function() {
    const hostelDetails = document.getElementById('hostelDetails');

    const hostels = [
        { name: 'Block A', capacity: 100, vacancy: 10 },
        { name: 'Block B', capacity: 150, vacancy: 20 }
    ];

    let detailsHTML = '<ul>';
    hostels.forEach(hostel => {
        detailsHTML += `<li>${hostel.name} - Capacity: ${hostel.capacity}, Vacancy: ${hostel.vacancy}</li>`;
    });
    detailsHTML += '</ul>';

    hostelDetails.innerHTML = detailsHTML;
});
