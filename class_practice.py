from unicodedata import name


class Patient():
    def __init__(self, name='Patient Name', age=-1, **kwargs):
        self.name = name
        self.age = age
        self.text_bracket = None
        self.ward_name = None
    def admission(self, ward_name):
        self.ward = ward_name


patient = Patient('Huzaifa Zahid', 6) 
print(f'Patient name is {patient.name}, he is {patient.age} years old')
patient.ward_name = 'Geastro'
print(f'Patient {patient.name} is now admitted in ward: {patient.ward_name}')
patient.ward_name = 'Neuro'
print(f'Patient {patient.name} is now admitted in ward: {patient.ward_name}')


class Student():
    def __init__(self, stuname="Student Name", stuage=-1, **kwargs):
        self.stuname = stuname
        self.stuage = stuage
        self.enrollment_number = None
    def enrolled(self, enrollment_number):
        self.enrollment_number = enrollment_number


student1 = Student("Fahad Zahid", 21)
print(f'Student name is {student1.stuname}, he is {student1.stuage} years old')
student1.enrollment_number =  'BG45678'
print(f'Student name is {student1.stuname}, he is {student1.stuage} years old. His enrollment number is {student1.enrollment_number}')
