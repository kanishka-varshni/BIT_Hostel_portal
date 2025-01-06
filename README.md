# 🏠 BIT Hostel Portal  

The **BIT Hostel Portal** is a comprehensive web application designed to streamline hostel management for students, wardens, and administrators. This portal integrates essential features such as room management, leave applications, feedback, and communication tools to ensure a seamless experience for all users.  

---

## ✨ Features  

### 🌟 **Login System**  
- Role-based login for **Students**, **Wardens**, and **Admins**.  
- 🔒 Secure authentication with Gmail ID integration for email-based communication.  

### 👩‍🎓 **Student Portal**  
- 🏠 **Dashboard**: Personalized welcome message (e.g., "Welcome, John Doe").  
- 📆 **Leave Application**: Apply for leave or extend existing leave with real-time status tracking.  
- 🛌 **Room Details**: View assigned room, floor, hostel, and fee payment details.  
- ✅ **Room Vacancy**: Check available rooms with color-coded indicators (🟢 Available, 🔴 Filled).  
- 📋 **Information Access**: View hostel facilities and contact details.  
- 📝 **Feedback**: Submit complaints or suggestions and track their resolution status.  

### 👨‍🏫 **Warden Portal**  
- 🏠 **Dashboard**: Overview of leave requests and personalized welcome message.  
- 🛌 **Room Details**: Access detailed student room information.  
- 📬 **Leave Approval**: Approve or reject student leave requests.  
- 🛏️ **Room Booking**: Verify room booking requests before sending them to the admin for final approval.  

### 🛡️ **Admin Portal**  
- 🏠 **Dashboard**: Comprehensive view of hostel statistics, including:  
  - 📊 Number of feedback received.  
  - 🚪 Room occupancy status.  
  - 🕒 Biometric attendance insights.  
- 🏢 **Hostel Management**: Add new hostels, rooms, or floors.  
- 🛌 **Room Bookings**: Finalize room bookings after warden verification.  
- 📨 **Communication**:  
  - Individual: Send emails to specific students.  
  - Group: Send announcements to a group of students.  
- 📋 **Leave Management**: View leave approvals from wardens with detailed student information.  
- 🧾 **Biometric Attendance**: Analyze attendance with insights like on-time, late, or absent students.  
- 📝 **Feedback Management**: Approve, reject, or mark feedback as "ongoing" or "completed".  

---

## 🛠️ Tech Stack  

### 💻 **Frontend**  
- HTML, CSS, JavaScript  

### ⚙️ **Backend**  
- Django Framework with RESTful API  

### 🗄️ **Database**  
- MySQL  

### 📧 **Email Integration**  
- Gmail SMTP for notifications and communication.  

---

## 🚀 Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/kanishka-varshni/BIT_Hostel_portal.git
   ```  

2. **Navigate to the project directory**:  
   ```bash
   cd BIT_Hostel_portal
   ```  

3. **Set up a virtual environment**:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```  

4. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```  

5. **Configure the database**:  
   - Update database credentials in the settings file.  
   - Run migrations:  
     ```bash
     python manage.py migrate
     ```  

6. **Start the development server**:  
   ```bash
   python manage.py runserver
   ```  

7. **Access the application**:  
   Open your browser and navigate to `http://127.0.0.1:8000/`.  

ed using Gmail SMTP.  

