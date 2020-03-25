"""Member calss.
This class represents a member object in the system. Its job is to store the personal information
associated with a specific member of certain organization(s).
"""

import Activity
import AttendanceRecord
import Administrator
import sendEmail as se
import WaitList


class Member:

    def __init__(self, name, student_ID, email_address, password, wait_list: WaitList):
        # initializing class member
        self.name = name
        self.email_address = email_address
        self.password = password
        self.__student_ID = student_ID
        self.wait_list = wait_list
        self.__attendanceRecord = []

    def get_name(self) -> str:
        # returns name of member: first name + last name
        return self.name


    def getID(self) -> str:
        # returns the student id of the member
        return self.student_ID

    def get_email_adderss(self) -> str:
        return self.email_address

    def get_password(self) -> str:
        return self.password


    #def getFaceID(self):  # -> FaceIdentification
        # returns the face id object of the member
        #return self.face_ID

    def averageScore(self):  # -> Score
        # returns the average attendance score of the member
        return self.score

    #def setFaceID(self, face_data):
        # sets the facial id data for the member
        #self.__face_ID = face_data

    def requestPermission(self, admin: Administrator) -> bool:
        se.send_email(self.email_address, 'placeholder', admin.get_email_adderss)
        self.wait_list.request_permit(self, admin)
        return True

    def joinActivity(self, activity: Activity) -> bool:
        # To do
        return True

    def attendanceRecord(self) -> AttendanceRecord:
        return self.attendanceRecord

    def __modifyAttendanceRecord(self) -> bool:
        # To do
        return True