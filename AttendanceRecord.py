from Activity import Activity
from datetime import datetime
from Member import Member

class AttendanceRecord:
    def __init__(self, activity: Activity, member: Member, status):
        self.activity = activity
        self.member = member
        self.status = status

    def get_activity(self):
        return self.activity

    def get_attendance_status(self):
        return self.status

    def take_attendance(self):
        arrival_time = datetime.now()
        
