from app.core.model.student import Student
from app.core.service.admission_service import AdmissionService
from app.core.model.parent import Parent
from app.core.model.bus import Bus


class StudenetService:
    def __init__(self, storage):
        self.storage = storage

    def addStudent(self, name, age, std, father, mother, location):
        students = self.storage.load()

        admission_no = AdmissionService.generate_admission_no(students)
        roll_no = AdmissionService.generate_roll_number(std, name, students)
        parent = Parent(father, mother)
        bus = Bus(location)
        new_student = Student(admission_no, roll_no, name, age, std, parent, bus)
        students.append(new_student.to_dict())
        self.storage.save(students)

        return new_student

    def showAllStudent(self):
        student = self.storage.load()

        for s in student:
            print("Student's Name => ", s["name"])

    def searchStudent(self):
        students = self.storage.load()
        admission_no = int(input("Enter admission number => "))
        if not admission_no:
            print("No data present")
            return
        for s in students:
            if s["admission_no"] == admission_no:
                print(f"Student name => {s["name"]}")
                print(f"Father's name => {s["parent"]["father_name"]}")
                return

        print("Student Found")

    def updateStudent(self):
        students = self.storage.load()
        admission_no = int(input("Enter the admission number => "))

        for student in students:
            if student["admission_no"] == admission_no:
                print("Student found!")

                student["name"] = input("Enter new name => ")
                self.storage.save(students)
                print("Student's information has been updated successfully")
                return

        print("Admission number is not found")
