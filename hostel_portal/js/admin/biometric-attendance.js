document.addEventListener('DOMContentLoaded', function() {
    const attendanceDetails = document.getElementById('attendanceDetails');

    const attendanceData = [
        { student: 'John Doe', status: 'Present', affixed: true },
        { student: 'Jane Smith', status: 'Absent', affixed: false }
    ];

    let detailsHTML = '<ul>';
    attendanceData.forEach(att => {
        detailsHTML += `<li>${att.student} - Status: ${att.status}, Affixed: ${att.affixed ? 'Yes' : 'No'}</li>`;
    });
    detailsHTML += '</ul>';

    attendanceDetails.innerHTML = detailsHTML;
});
