import mysql.connector


class data:
    def __init__(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()

        query = """
                CREATE TABLE IF NOT EXISTS Students_details(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(40),
                course VARCHAR(20),
                cgpa FLOAT,
                placementStatus VARCHAR(20)
        ) 
        """
        cursor.execute(query)
        conn.commit()

        cursor.close()
        conn.close()

    def insertStudent(self, student):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()

        query = """
        INSERT INTO Students_details (name, course, cgpa, placementStatus) 
        VALUES (%s, %s, %s, %s)
        """
        values = (
            student.get_name(),
            student.get_course(),
            student.get_cgpa(),
            student.get_placementStatus(),
        )

        # Don't insert if validation failed in the Student class
        if None not in values:
            cursor.execute(query, values)
            conn.commit()
            print("Student inserted successfully.")
        else:
            print("Failed to insert: Invalid student data.")

        cursor.close()
        conn.close()

    def updatePlacement(self, student_id, status):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()

        query = "UPDATE Students_details SET placementStatus = %s WHERE id = %s"
        cursor.execute(query, (status, student_id))
        conn.commit()

        cursor.close()
        conn.close()

    def updateData(self, student_id, student):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()

        values = (student.get_name(), student.get_course(), student.get_cgpa())

        if None not in values:
            query = "UPDATE Students_details SET name = %s, course = %s, cgpa = %s WHERE id = %s"
            cursor.execute(query, values + (student_id,))
            conn.commit()

        cursor.close()
        conn.close()

    def deleteStudent(self, student_id):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()
        query = "DELETE FROM Students_details WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()

        cursor.close()
        conn.close()

    def viewAllStudents(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM Students_details"
        cursor.execute(query)

        records = cursor.fetchall()  # Grab the data

        cursor.close()
        conn.close()

        return records  # Return the data so the GUI can use it

    def cleardata(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Sam@2286", database="Student_db"
        )
        cursor = conn.cursor()
        cursor.execute("TRUNCATE table Students_details")

        cursor.close()
        conn.close()
