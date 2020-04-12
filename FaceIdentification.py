import face_recognition
import numpy
import os
from ecapture import ecapture as ec


class FaceIdentification:

    def __init__(self):
        self.face_id = None

    #return true if face id is successfully set
    def set_face_id(self, member_id) -> bool:
        ec.capture(1, "your face id", member_id + ".jpg")
        member_image = face_recognition.load_image_file(member_id + ".jpg")
        self.face_id = face_recognition.face_encodings(member_image)[0].tostring()
        return self.test_face_is_set()

    def compare_to(self, image):
        this_encoding = numpy.fromstring(self.face_id)
        other_encoding = face_recognition.face_encodings(image)[0]
        return face_recognition.compare_faces([this_encoding], other_encoding)

    def test_face_is_set(self):
        ec.capture(1, False, "tester.jpg")
        tester = face_recognition.load_image_file("tester.jpg")
        this_encoding = numpy.fromstring(self.face_id)
        tester_encoding = face_recognition.face_encodings(tester)[0]
        result = face_recognition.compare_faces([this_encoding], tester_encoding)
        os.remove("tester.jpg")
        return result
