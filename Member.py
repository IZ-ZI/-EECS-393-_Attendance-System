"""Member class.
This class represents a member object in the system. Its job is to store the personal information
associated with a specific member of certain organization(s).
"""
from Activity import Activity
from Administrator import Administrator
# from FaceIdentification import FaceIdentification
import sendEmail as se


class Member:

    def __init__(self, name, student_ID, email_address, password):
        # initializing class member
        self.name = name
        self.email_address = email_address
        self.password = password
        self.student_ID = student_ID
        self.score = 0
        self.admin_list = []
        self.face_id = ''

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


    # def get_face_id(self) -> FaceIdentification:
    #     return self.face_id




