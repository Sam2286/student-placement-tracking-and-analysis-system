class Students:
    courses = ["ai", "it", "bda"]

    def __init__(self):
        self.__name = None
        self.__course = None
        self.__cgpa = None
        self.__placementStatus = "No"

    # --- GETTERS ---
    def get_name(self):
        return self.__name

    def get_course(self):
        return self.__course

    def get_cgpa(self):
        return self.__cgpa

    def get_placementStatus(self):
        return self.__placementStatus

    # --- SETTERS ---
    def set_name(self, name):
        self.__name = name

    def set_course(self, course):
        # Converted to lower to match your list safely
        if course.lower() in Students.courses:
            self.__course = course.lower()
        else:
            self.__course = None  # Keep as None if invalid

    def set_cgpa(self, cgpa):
        if 0.0 <= cgpa <= 10.0:
            self.__cgpa = cgpa
        else:
            self.__cgpa = None  # Keep as None if invalid

    def set_placementStatus(self, status):
        if status=="yes" or status=="no":
            self.__placementStatus = status
        else:
            print("invalid input")
