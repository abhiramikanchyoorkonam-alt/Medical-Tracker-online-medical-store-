Medicine Management System

This project is a web-based application for managing medicines, user registrations, and contact messages. It provides an admin dashboard for adding, editing, and deleting medicine details, while also displaying user registrations and contact messages.

Features
Medicine Management: Add, edit, and delete medicine records (including name, dosage, price, and dates).
User Registrations: View all registered users, including their personal details.
Contact Messages: View messages sent by users via the contact form.
Admin and User Login: Admin login (username: admin, password: password) with access to the dashboard; registered users also have a separate user interface.
Technologies Used
Django: Backend framework for routing, models, and views.
Python: Core language for the backend logic.
SQLite: Default lightweight database for storing medicines, users, and messages.
HTML/CSS: Frontend structure and styling.
Django Forms: For secure user input and validation.
Setup
Clone this repository to your local machine.
Ensure you have Python and Django installed.
Run python manage.py migrate to set up the database.
Create a superuser with python manage.py createsuperuser to access the admin dashboard.
Run the server: python manage.py runserver.
Visit http://127.0.0.1:8000/to access the dashboard.
Future Improvements
Add user authentication for registered users.
Implement password hashing for security.
Add search and filtering for medicines and user lists.
