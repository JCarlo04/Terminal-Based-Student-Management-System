class SearchStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def search_student(self, name):
        for student in self.student_data.allstudents:
            if student["name"].lower() == name.lower():
                return f'Name: {student["name"]}, Age: {student["age"]}, ID: {student["idnum"]}, Email: {student["email"]}, Phone: {student["phone"]}'
        return "Student not found."