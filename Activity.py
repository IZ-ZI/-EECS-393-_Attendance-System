from datetime import datetime

class Activity:
    def __init__(self, id, name, start_time: datetime, end_time: datetime, location):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def get_id(self):
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_location(self):
        return self.location
