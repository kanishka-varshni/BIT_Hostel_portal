document.getElementById('studentSearchForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const rollNumber = document.getElementById('roll_number').value;
    const studentName = document.getElementById('student_name').value;

    alert(`Searched for Student: ${studentName} (Roll Number: ${rollNumber})`);
});
