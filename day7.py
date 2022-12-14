
class person:
    name = ""
    age = 0
    address = ""
    phone = 123456789
    def __init__(self, name, age, address, phone):
         self.name = name
         self.age = age
         self.address = address
         self.phone = phone
    def printValue(self):
        print(self.name, self.age, self.address, self.phone)

person1 = person("Liakot", 27, "HSTU", 1797681231)
person1.printValue()

class student(person):
    studentId = 100000
    department = ""
    institution = ""
    def __init__(self, name, age, address, phone, sid, dept, ins):
        super().__init__(name, age, address, phone)
        self.studentId = sid
        self.department = dept
        self.institution = ins
    def printStudent(self):
        print(self.studentId, self.department, self.institution)

stu1 = student(name="Liakot", age=24, phone=1797681231, address="Dinajpur", sid=1802035, ins="HSTU", dept="CSE")
print("\nInformation from person class:")
stu1.printValue()
print("\nInformation from student class:")
stu1.printStudent()

class teacher(person):
    teacherId = 20000
    major = ""
    instituition = ""
    def __init__(self, name, age, address, phone, tid, major, ins):
        super().__init__(name, age, address, phone)
        self.teacherId = tid
        self.major = major
        self.institution = ins
    def printTeacher(self):
        print(self.teacherId, self.major, self.institution)

teacher1 = teacher(name="Nahid Sultan", age=34, phone=1797681231, address="Dinajpur", tid=1002032, ins="HSTU", major="CSE")
print("\nInformation from person class:")
teacher1.printValue()
print("\nInformation from teacher class:")
teacher1.printTeacher()