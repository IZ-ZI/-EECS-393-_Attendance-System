import face_recognition
from ecapture import ecapture as ec


class FaceIdentification:

    def __init__(self):
        self.face_id = None

    def set_face_id(self, name):
        ec.capture(1, False, name + ".jpg")
        self.face_id = face_recognition.load_image_file(name + ".jpg")

    def compare_to(self, image):
        this_encoding = face_recognition.face_encodings(self.face_id)[0]
        other_encoding = face_recognition.face_encodings(image)[0]
        return face_recognition.compare_faces([this_encoding], other_encoding)
