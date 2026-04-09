class Student:
    def __init__(self, admission_no, roll_no, name, age, std, parent, bus):
        self.admission_no = admission_no
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.std = std
        self.parent = parent
        self.bus = bus

    def to_dict(self):
        return {
            "admission_no": self.admission_no,
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "std": self.std,
            "parent": self.parent.to_dict(),
            "bus": self.bus.to_dict(),
        }
