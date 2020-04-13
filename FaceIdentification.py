import face_recognition


class FaceIdentification:

    @staticmethod
    def compare_to(encoding1, encoding2):
        return face_recognition.compare_faces([encoding1], encoding2)

    @staticmethod
    def encoding_from_photo(photo):
        try:
            encoding = face_recognition.face_encodings(photo)[0].tostring()
        except: # no face found
            print("encoding fail")
            return None
        return encoding
