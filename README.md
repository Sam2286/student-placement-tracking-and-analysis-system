
## Student Management Dashboard (Python Tkinter)

## Project Overview
This project is a Student Management Dashboard developed using Python Tkinter GUI with database connectivity. It is designed for an admin to manage student records efficiently. The application supports complete CRUD operations such as adding, viewing, updating, and deleting student information. It also includes placement status management and graphical visualization of student data.

## Project Objectives
- To create a GUI-based student record management system.
- To store and manage student data using a database.
- To provide an easy admin dashboard for student operations.
- To visualize student-related data using charts.

## Key Features
- Add New Student (Name, Course, CGPA)
- View All Students in Table Format
- Update Student Details using Student ID
- Update Placement Status (Yes / No)
- Delete Student Record using Student ID
- Clear All Student Data (Admin confirmation required)
- Scatter Plot Visualization
- Pie Chart Visualization

## Technologies Used
- Python
- Tkinter (GUI Development)
- SQLite / Database Module
- Matplotlib (Data Visualization)
- OOP Concepts (Student Class)

## Modules Used in Project

## 1. Students.py
Contains the Students class with setter and getter methods for:
- Name
- Course
- CGPA

## 2. database.py
Handles all database-related operations:
- Insert student
- View student list
- Update student data
- Update placement status
- Delete student
- Clear complete data

## 3. visualization.py
Handles data visualization functions:
- Scatter Plot
- Pie Chart

## 4. main.py
Main GUI dashboard file that contains all buttons and Tkinter windows for performing operations.

## Working of Application
The admin dashboard provides multiple buttons for performing different tasks. When a button is clicked, a new Tkinter window opens for that operation. The data entered by the admin is validated and then stored/updated in the database. The application also provides charts to visually represent student performance and placement statistics.

## Visualizations Included
- Scatter Plot: Used to analyze student CGPA distribution.
- Pie Chart: Used to show placement status or course distribution.

## Input Validation
The project validates inputs to avoid incorrect data entry such as:
- Invalid CGPA values
- Invalid course input
- Incorrect Student ID during update/delete

## Conclusion
This Student Management Dashboard is a simple and effective system for managing student details using a GUI interface. It demonstrates the practical implementation of Tkinter GUI, database connectivity, and data visualization in Python.
