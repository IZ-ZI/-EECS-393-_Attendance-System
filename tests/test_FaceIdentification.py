from unittest import TestCase
from FaceIdentification import FaceIdentification as fi
import face_recognition
import os


class TestFaceIdentification(TestCase):

    photo1 = face_recognition.load_image_file(os.path.abspath("ha.png"))
    photo2 = face_recognition.load_image_file(os.path.abspath("y_ha.png"))
    photo3 = face_recognition.load_image_file(os.path.abspath("trump.png"))
    photo4 = face_recognition.load_image_file(os.path.abspath("cwru.png"))
    encoding1 = face_recognition.face_encodings(photo1)[0].tostring()
    encoding2 = face_recognition.face_encodings(photo2)[0].tostring()
    encoding3 = face_recognition.face_encodings(photo3)[0].tostring()

    def test_compare_to(self):
        self.assertTrue(fi.compare_to(self.encoding1, self.encoding2))
        self.assertFalse(fi.compare_to(self.encoding1, self.encoding3))

    def test_encoding_from_photo(self):
        encoding = fi.encoding_from_photo(self.photo4)
        self.assertTrue(encoding == None)
        self.assertTrue(self.encoding1 == fi.encoding_from_photo(self.photo1))
