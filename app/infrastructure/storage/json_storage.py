import json
import os
from app.core.interface.storage_interface import StorageInterface


class JSONStorage(StorageInterface):
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath) as f:
            return json.load(f)

    def save(self, data):
        with open(self.filepath, "w") as f:
            return json.dump(data, f, indent=4)
