import face_recognition
import numpy

class FaceIdentification:

    @staticmethod
    def compare_to(encoding1, encoding2):
        encoding_1 = numpy.frombuffer(encoding1)
        encoding_2 = numpy.frombuffer(encoding2)
        result = face_recognition.compare_faces([encoding_1], encoding_2)
        return result[0]

    @staticmethod
    def encoding_from_photo(photo) -> str:
        try:
            encoding = face_recognition.face_encodings(photo)[0].tostring()
        except: # no face found
            print("encoding fail")
            return " "
        return encoding
