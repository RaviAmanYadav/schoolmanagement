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
