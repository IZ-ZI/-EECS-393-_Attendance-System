import face_recognition
import numpy

class FaceIdentification:

    @staticmethod
    def compare_to(encoding1, encoding2):
        if encoding1 is None or encoding2 is None:
            return False;
        encoding_1 = numpy.fromstring(encoding1)
        encoding_2 = numpy.fromstring(encoding2)
        result = face_recognition.compare_faces([encoding_1], encoding_2)
        return result[0]

    @staticmethod
    def encoding_from_photo(photo):
        try:
            encoding = face_recognition.face_encodings(photo)[0].tostring()
        except: # no face found
            print("encoding fail")
            return None
        return encoding
