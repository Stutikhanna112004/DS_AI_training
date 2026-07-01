from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    @abstractmethod
    def cal_fees(self):
        pass

    @abstractmethod
    def get_attendance_requiremant(self):
        pass

    def get_profiles(self):
        return f"ID : {self.student_id} | Name : {self.name}"


class Reg_student(Student):
    def cal_fees(self):
        return "Tuition : 10000 + hostel : 30000"

    def get_attendance_requiremant(self):
        return "Minimum 85% attendance is mandatory"


class DistanceStudent(Student):
    def cal_fees(self):
        return "Tuition : 10000"

    def get_attendance_requiremant(self):
        return "No required per day classes"


Student_a = Reg_student("Shashwat Pandey", "REG2022-65")
Student_b = DistanceStudent("Stuti Khanna", "DSI2026-38")

print(Student_a.get_profiles())
print(Student_a.get_attendance_requiremant())
print(Student_b.get_profiles())
print(Student_b.get_attendance_requiremant())