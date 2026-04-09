class Bus:
    FEES = {"near": 500, "mid": 1000, "far": 1500}

    def __init__(self, location):
        self.location = location
        self.fee = self.FEES.get(location, 0)

    def to_dict(self):
        return {"location": self.location, "fee": self.fee}
