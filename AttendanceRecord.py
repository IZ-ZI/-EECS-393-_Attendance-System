from Activity import Activity
from datetime import datetime
from Member import Member
from Status import Status
from FaceIdentification import FaceIdentification


class AttendanceRecord:
    def __init__(self, activity: Activity, member: Member):
        self.activity = activity
        self.member = member
        self.status = status

    def get_activity(self):
        return self.activity

    def get_attendance_status(self):
        return self.status

    def take_attendance(self):
        current_status = figured_status(datetime.now())
        taken_face = FaceIdentification()
        taken_face.set_face_id()

        if not member.get_face_id().compare_to(taken_face):
            return false
        else:
            self.status = current_status

    def figured_status(self, time: datetime):
        if time <= activity.get_start_time():
            return Status.on_time

        elif time <= activity.get_end_time():
            return Status.late

        else:
            return Status.absent


