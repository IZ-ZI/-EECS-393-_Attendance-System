"""Member class.
This class represents a member object in the system. Its job is to store the personal information
associated with a specific member of certain organization(s).
"""
from Activity import Activity
from AttendanceRecord import AttendanceRecord
from Administrator import Administrator
from FaceIdentification import FaceIdentification
import sendEmail as se


class Member:

    def __init__(self, name, student_ID, email_address, password):
        # initializing class member
        self.name = name
        self.email_address = email_address
        self.password = password
        self.student_ID = student_ID
        self.score = 0
        self.attendance_record = []
        self.admin_list = []
        self.face_id = FaceIdentification();

    def get_name(self) -> str:
        # returns name of member: first name + last name
        return self.name

    def get_id(self) -> str:
        # returns the student id of the member
        return self.student_ID

    def get_email_address(self) -> str:
        return self.email_address

    def get_password(self) -> str:
        return self.password

    def get_admin_list(self) -> list:
        return self.admin_list

    def averageScore(self):  # -> Score
        # returns the average attendance score of the member
        return self.score

    def get_face_id(self) -> FaceIdentification:
        return self.face_id

    def set_face_id(self) -> bool:
        successful_set = self.face_id.set_face_id(self.get_id())

        trial = 0
        while not successful_set and trial != 3:  # give up after 3 unsuccessful trials
            self.face_id.set_face_id(self.get_id())
            trial = trial + 1
        return successful_set

    def requestPermission(self, admin: Administrator) -> bool:
        se.send_email('attsystem393@gmail.com', 'eecs_393', admin.get_email_adderss(), self.get_name(), self.get_id(), True)
        return True

    def joinActivity(self, activity: Activity) -> bool:
        # To do
        return True

    def attendanceRecord(self) -> list:
        return self.attendance_record

    def __modifyAttendanceRecord(self) -> bool:
        # To do
        return True
