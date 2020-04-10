class AttendanceRecord:
    def __init__(self, activity, status):
        self.activity = activity
        self.status = status

    def get_arrival_time(self):
        return self.time

    def get_attendance_status(self):
        return self.status
