"""Member calss.
This class represents a member object in the system. Its job is to store the personal information
associated with a specific member of certain organization(s).
"""
import Activity
import AttendanceRecord


class Member:

    def __init__(self, first_name, last_name, student_ID, face_ID, score):
        # initializing class member
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__face_ID = face_ID
        self.__score = score
        self.__attendanceRecord = []

    def getName(self) -> str:
        # returns name of member: first name + last name
        return "%s %s" % (self.first_name, self.last_name)

    def getID(self) -> int:
        # returns the student id of the member
        return self.student_ID

    def getFaceID(self):  # -> FaceIdentification
        # returns the face id object of the member
        return self.face_ID

    def averageScore(self):  # -> Score
        # returns the average attendance score of the member
        return self.score

    def setFaceID(self, face_data):
        # sets the facial id data for the member
        self.__face_ID = face_data

    def requestPermission(self) -> bool:
        # To do
        return True

    def joinActivity(self, activity: Activity) -> bool:
        # To do
        return True

    def attendanceRecord(self) -> AttendanceRecord:
        return self.attendanceRecord

    def __modifyAttendanceRecord(self) -> bool:
        # To do
        return True