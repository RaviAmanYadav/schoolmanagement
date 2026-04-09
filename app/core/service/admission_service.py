class AdmissionService:
    @staticmethod
    def generate_admission_no(student):
        return len(student) + 1

    @staticmethod
    def generate_roll_number(std, name, students):
        same_class = [s for s in students if s["class"] == std]
        same_class.sort(key=lambda x: x[name])
        return f"{std}-{len(same_class)+1}"
