import face_recognition
import numpy
import os
from ecapture import ecapture as ec


class FaceIdentification:

    # return true if face id is successfully set
    def set_face_id(self, member_id: str) -> str:

        ec.capture(1, "your face id", member_id + ".jpg")
        member_image = face_recognition.load_image_file(member_id + ".jpg")
        try:
            face_id = face_recognition.face_encodings(member_image)[0].tostring()
        except:
            return None  # face id is not set, error reading faces from the camera
        return face_id

    def compare_to(self, encoding1, encoding2):
        return face_recognition.compare_faces([encoding1], encoding2)

    @staticmethod
    def encoding_from_photo(photo):
        try:
            encoding = face_recognition.face_encodings(photo)[0].tostring()
        except: # no face found
            print("encoding fail")
            return None
        return encoding
