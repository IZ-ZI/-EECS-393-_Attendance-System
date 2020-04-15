from Activity import Activity
from datetime import datetime
from ecapture import ecapture as ec
import face_recognition
import os
from FaceIdentification import FaceIdentification


class AttendanceRecord:
    def __init__(self, activity: Activity):
        self.activity = activity
        self.status = ""

    def get_activity(self):
        return self.activity

    def get_status(self):
        return self.status

    def take_attendance(self, member):
        current_status = self.figured_status(datetime.now())
        ec.capture(1, "photo taken", "taken_face.jpg")
        taken_face = face_recognition.load_image_file("taken_face.jpg")
        if not member.get_face_id().compare_to(taken_face):
            os.remove("taken_face.jpg")
            return True
        else:
            self.status = current_status
            os.remove("taken_face.jpg")
            return True

    def figured_status(self, time: datetime):
        if time <= self.activity.get_start_time():
            return "on_time"

        elif time <= self.activity.get_end_time():
            return "late"

        else:
            return "absent"


