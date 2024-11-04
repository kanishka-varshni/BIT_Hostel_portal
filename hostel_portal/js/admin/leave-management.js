document.addEventListener('DOMContentLoaded', function() {
    const leaveRequests = document.getElementById('leaveRequests');

    const requests = [
        { student: 'John Doe', type: 'Sick Leave', dates: '2024-08-01 to 2024-08-03' },
        { student: 'Jane Smith', type: 'Casual Leave', dates: '2024-08-10 to 2024-08-12' }
    ];

    let requestsHTML = '<ul>';
    requests.forEach(request => {
        requestsHTML += `<li>${request.student} - ${request.type} - Dates: ${request.dates}</li>`;
    });
    requestsHTML += '</ul>';

    leaveRequests.innerHTML = requestsHTML;
});
