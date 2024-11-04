-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS bit_hostel_portal;
USE bit_hostel_portal;

-- USERS TABLE (For authentication purposes)
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('student', 'warden', 'admin') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- STUDENTS TABLE
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    address VARCHAR(100),
    contact_number VARCHAR(15),
    hostel_id INT,
    room_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- WARDENS TABLE
CREATE TABLE Wardens (
    warden_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    contact_number VARCHAR(15),
    hostel_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- HOSTELS TABLE
CREATE TABLE Hostels (
    hostel_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(100)
);

-- ROOMS TABLE
CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    hostel_id INT NOT NULL,
    floor_number INT,
    room_number VARCHAR(10),
    capacity INT,
    occupied INT DEFAULT 0,
    FOREIGN KEY (hostel_id) REFERENCES Hostels(hostel_id) ON DELETE CASCADE
);

-- LEAVE REQUESTS TABLE
CREATE TABLE LeaveRequests (
    leave_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    from_date DATE,
    to_date DATE,
    reason TEXT,
    leave_type ENUM('on duty', 'internal od', 'internal training') NOT NULL,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE
);

-- FEEDBACK TABLE
CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    content TEXT,
    status ENUM('pending', 'ongoing', 'completed', 'rejected') DEFAULT 'pending',
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE
);

-- SAMPLE DATA

-- INSERT SAMPLE USERS (Admin, Warden, and Students)
INSERT INTO Users (name, email, username, password_hash, role) VALUES
('Kanishka', 'kanishka@gmail.com', 'kanishka', 'hashed_password1', 'student'),
('Varshni', 'varshni@gmail.com', 'varshni', 'hashed_password2', 'student'),
('Pravin', 'pravin@gmail.com', 'pravin', 'hashed_password3', 'student'),
('Harish', 'harish@gmail.com', 'harish', 'hashed_password4', 'student'),
('Warden1', 'warden1@gmail.com', 'warden1', 'hashed_password5', 'warden'),
('Admin', 'admin@gmail.com', 'admin', 'hashed_password6', 'admin');

-- INSERT SAMPLE HOSTELS
INSERT INTO Hostels (name, location) VALUES
('Alpha Hostel', 'Coimbatore'),
('Beta Hostel', 'Erode');

-- INSERT SAMPLE ROOMS
INSERT INTO Rooms (hostel_id, floor_number, room_number, capacity, occupied) VALUES
(1, 1, '101', 2, 1),
(1, 2, '202', 2, 2),
(2, 1, '103', 3, 1);

-- INSERT SAMPLE STUDENTS
INSERT INTO Students (user_id, address, contact_number, hostel_id, room_id) VALUES
(1, 'Coimbatore', '9876543210', 1, 1),
(2, 'Erode', '9876543211', 1, 2),
(3, 'Coimbatore', '9876543212', 2, 3),
(4, 'Erode', '9876543213', 2, 1);

-- INSERT SAMPLE WARDEN
INSERT INTO Wardens (user_id, contact_number, hostel_id) VALUES
(5, '9876543214', 1);

-- INSERT SAMPLE LEAVE REQUESTS
INSERT INTO LeaveRequests (student_id, from_date, to_date, reason, leave_type) VALUES
(1, '2024-10-25', '2024-10-28', 'Medical leave', 'on duty'),
(2, '2024-11-01', '2024-11-05', 'Training', 'internal training');

-- INSERT SAMPLE FEEDBACK
INSERT INTO Feedback (student_id, content) VALUES
(1, 'The food quality needs improvement.'),
(3, 'Please provide better Wi-Fi connectivity.');
