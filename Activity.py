from datetime import datetime


class Activity:
    def __init__(self, name, start_time: datetime, end_time: datetime, location, priority):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.priority = priority

    def get_name(self) -> str:
        return self.name

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_location(self):
        return self.location

    def get_priority(self):
        return self.priority