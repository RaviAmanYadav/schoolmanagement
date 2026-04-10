from app.infrastructure.storage.json_storage import JSONStorage
from app.core.service.student_service import StudenetService


def run():
    storage = JSONStorage("data/student.json")
    service = StudenetService(storage)

    while True:
        print("1. Add students")
        print("2. Show all studentss")
        print("3. Search Student")
        print("4. Update Student details")
        print("5. Exit")
        choice = int(input("Enter your choice => "))

        match choice:
            case 1:
                name = input("Enter student's name => ")
                age = int(input("Enter age => "))
                std = input("Enter your class => ")
                father = input("Enter your father's name => ")
                mother = input("Enter your mother's name => ")
                location = input("Enter location (near/mid/far) => ")
                service.addStudent(name, age, std, father, mother, location)
            case 2:
                service.showAllStudent()
            case 3:
                service.searchStudent()
            case 4:
                service.updateStudent()
            case 5:
                exit()
            case _:
                print("Invalid operation.")
