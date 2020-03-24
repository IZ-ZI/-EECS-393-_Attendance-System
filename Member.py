"""Member calss.
This class represents a member object in the system. Its job is to store the personal information
associated with a specific member of certain organization(s).
"""
import Activity as Activity
import AttendanceRecord as AttendanceRecord

class Member:
    memberCount = 0

    def _init_(self, first_name, last_name, student_ID, face_ID, score):
        # initializing class member
        self.first_name = first_name
        self.last_name = last_name
        self.student_ID = student_ID
        self.face_ID = face_ID
        self.score = score
        self.attendanceRecord = AttendanceRecord()
        Member.memberCount += 1

    def get_name(self) -> str:
        # returns name of member: first name + last name
        return "%s %s" % (self.first_name, self.last_name)

    def get_id(self) -> int:
        # returns the student id of the member
        return self.student_ID

    def getFaceID(self): # -> FaceIdentification
        # returns the face id object of the member
        return self.face_ID

    def averageScore(self): # -> Score
        # returns the average attendance score of the member
        return self.score

    def setFaceID(self, face_data):
        # sets the facial id data for the member
        self.face_ID = face_data

    def requestPermission(self) -> bool:
        # To do
        return True

    def joinActivity(self, activity: Activity) -> bool:
        #To do
        return True

    def attendanceRecord(self) -> AttendanceRecord:
        return self.attendanceRecord

    def __modifyAttendanceRecord(self) -> bool:
        # To do
        return True




