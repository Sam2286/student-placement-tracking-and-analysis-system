import mysql.connector
import matplotlib.pyplot as plt


def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sam@2286",   # use SAME password everywhere
        database="student_db"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT name, cgpa, placementStatus FROM Students_details")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# 🔹 Scatter Plot: CGPA vs Placement
def show_scatter():
    data = fetch_data()

    cgpa = []
    placement = []

    for row in data:
        cgpa.append(row[1])
        # Convert Yes/No to 1/0
        placement.append(1 if row[2] == "Yes" else 0)

    plt.figure()
    plt.scatter(cgpa, placement)

    plt.xlabel("CGPA")
    plt.ylabel("Placement (1=Yes, 0=No)")
    plt.title("CGPA vs Placement Status")

    plt.show()


# 🔹 Pie Chart: Placement Distribution
def show_pie():
    data = fetch_data()

    placed = 0
    not_placed = 0

    for row in data:
        if row[2] == "Yes":
            placed += 1
        else:
            not_placed += 1

    labels = ["Placed", "Not Placed"]
    values = [placed, not_placed]

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.title("Placement Distribution")

    plt.show()