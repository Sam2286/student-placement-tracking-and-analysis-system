import tkinter as tk
from tkinter import messagebox, ttk
from Students import Students
from database import data
import visualization


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management Dashboard")
        self.root.geometry("400x600")

        # Connect to DB
        self.db = data()

        # Title
        title = tk.Label(self.root, text="Admin Dashboard", font=("Arial", 20, "bold"))
        title.pack(pady=20)

        # -------- MAIN BUTTONS --------
        tk.Button(self.root, text="Add New Student", width=20, command=self.open_add_window).pack(pady=10)

        tk.Button(self.root, text="View All Students", width=20, command=self.open_view_window).pack(pady=10)

        tk.Button(self.root, text="Update Student Data", width=20, command=self.open_update_window).pack(pady=10)

        tk.Button(self.root, text="Update Placement Status", width=20, command=self.open_placement_window).pack(pady=10)

        tk.Button(self.root, text="Delete a Student", width=20, command=self.open_delete_window).pack(pady=10)

        # -------- GRAPH BUTTONS --------
        tk.Button(
            self.root,
            text="Show Scatter Plot",
            width=20,
            command=visualization.show_scatter
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Show Pie Chart",
            width=20,
            command=visualization.show_pie
        ).pack(pady=10)

        # -------- EXIT (SECOND LAST) --------
        tk.Button(
            self.root,
            text="Exit",
            width=20,
            command=self.root.quit
        ).pack(pady=10)

        # -------- CLEAR DATA (LAST) --------
        tk.Button(
            self.root,
            text="Clear ALL Data",
            width=20,
            bg="red",
            fg="white",
            command=self.clear_all_action
        ).pack(pady=10)

    # -------- ADD STUDENT --------
    def open_add_window(self):
        win = tk.Toplevel(self.root)
        win.title("Add Student")
        win.geometry("300x300")

        tk.Label(win, text="Name").pack()
        name = tk.Entry(win)
        name.pack()

        tk.Label(win, text="Course (ai/it/bda)").pack()
        course = tk.Entry(win)
        course.pack()

        tk.Label(win, text="CGPA").pack()
        cgpa = tk.Entry(win)
        cgpa.pack()

        def submit():
            try:
                student = Students()
                student.set_name(name.get())
                student.set_course(course.get())
                student.set_cgpa(float(cgpa.get()))

                if student.get_course() is None or student.get_cgpa() is None:
                    messagebox.showerror("Error", "Invalid input")
                    return

                self.db.insertStudent(student)
                messagebox.showinfo("Success", "Student Added")
                win.destroy()

            except:
                messagebox.showerror("Error", "Invalid Input")

        tk.Button(win, text="Submit", command=submit).pack(pady=10)

    # -------- VIEW STUDENTS --------
    def open_view_window(self):
        win = tk.Toplevel(self.root)
        win.geometry("600x300")

        columns = ("ID", "Name", "Course", "CGPA", "Placement")
        tree = ttk.Treeview(win, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        tree.pack(fill=tk.BOTH, expand=True)

        records = self.db.viewAllStudents()

        for row in records:
            tree.insert("", tk.END, values=row)

    # -------- UPDATE STUDENT --------
    def open_update_window(self):
        win = tk.Toplevel(self.root)

        tk.Label(win, text="ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        tk.Label(win, text="Name").pack()
        name = tk.Entry(win)
        name.pack()

        tk.Label(win, text="Course").pack()
        course = tk.Entry(win)
        course.pack()

        tk.Label(win, text="CGPA").pack()
        cgpa = tk.Entry(win)
        cgpa.pack()

        def update():
            try:
                student = Students()
                student.set_name(name.get())
                student.set_course(course.get())
                student.set_cgpa(float(cgpa.get()))

                self.db.updateData(int(id_entry.get()), student)
                messagebox.showinfo("Updated", "Student Updated")

            except:
                messagebox.showerror("Error", "Invalid Input")

        tk.Button(win, text="Update", command=update).pack(pady=10)

    # -------- DELETE --------
    def open_delete_window(self):
        win = tk.Toplevel(self.root)

        tk.Label(win, text="Student ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        def delete():
            try:
                self.db.deleteStudent(int(id_entry.get()))
                messagebox.showinfo("Deleted", "Student Deleted")

            except:
                messagebox.showerror("Error", "Invalid ID")

        tk.Button(win, text="Delete", command=delete).pack(pady=10)

    # -------- PLACEMENT --------
    def open_placement_window(self):
        win = tk.Toplevel(self.root)

        tk.Label(win, text="Student ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        status = ttk.Combobox(win, values=["Yes", "No"])
        status.pack()

        def update():
            try:
                self.db.updatePlacement(int(id_entry.get()), status.get())
                messagebox.showinfo("Updated", "Placement Updated")

            except:
                messagebox.showerror("Error", "Invalid Input")

        tk.Button(win, text="Update", command=update).pack(pady=10)

    # -------- CLEAR --------
    def clear_all_action(self):
        confirm = messagebox.askyesno(
            "⚠ WARNING",
            "Are you sure you want to delete ALL student data?\n\nThis cannot be undone!"
        )

        if confirm:
            self.db.cleardata()
            messagebox.showinfo("Success", "All student data deleted successfully!")


# -------- RUN APP --------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()