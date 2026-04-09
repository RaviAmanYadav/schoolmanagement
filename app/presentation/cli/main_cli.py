from app.infrastructure.storage.json_storage import JSONStorage
from app.core.service.student_service import StudenetService


def run():
    storage = JSONStorage("data/students.json")
    service = StudenetService(storage)

    while True:
        print("\n1. Add Student\n2. Exit")
        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            std = input("Class: ")
            father = input("Father: ")
            mother = input("Mother: ")
            location = input("Bus (near/mid/far): ")

            student = service.addStudent(name, age, std, father, mother, location)
            print("Added:", student.to_dict())

        elif choice == "2":
            break
