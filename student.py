class StudentInfo:
    def __init__(self):
        self.allstudents = []

    def setFirstName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhoneNumber(self, phone):
        self.phone = phone

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getIDNum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone Number: {self.phone}"

    def read(self):
        with open("studentlist.txt", "r") as f:
            read = f.readlines()

            for i in read[0:]:
                load = StudentInfo()
                line_strip = i.strip().split(",")
                load.setFirstName(line_strip[0])
                load.setAge(line_strip[1])
                load.setIDNum(line_strip[2])
                load.setEmail(line_strip[3])
                load.setPhoneNumber(line_strip[4])
                self.allstudents.append(load)
