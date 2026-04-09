class Parent:
    def __init__(self, fname: str, mname: str):
        self.fname = fname
        self.mname = mname

    def to_dict(self):
        return {"father_name": self.fname, "mother_name": self.mname}
