class Login:
    def __init__(self, student):
        self.student_data = student

    def login(self, id_number):
        for student in self.student_data.allstudents:
            if student.idnum == id_number:
                return student
        raise Exception