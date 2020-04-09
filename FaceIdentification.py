import face_recognition
from ecapture import ecapture as ec


class FaceIdentification:

    def __init__(self):
        self.face_id = None

    def set_face_id(self):
        ec.delay_imcapture(0, "Hold still while taking the picture", "id", 3)
        self.face_id = face_recognition.load_image_file("id.jpg")

    def compare_to(self, image):
        this_encoding = face_recognition.face_encodings(self.face_id)[0]
        other_encoding = face_recognition.face_encodings(image)[0]
        return face_recognition.compare_faces([this_encoding], other_encoding)
