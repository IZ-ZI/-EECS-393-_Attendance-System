from FaceIdentification import FaceIdentification
import face_recognition
from Activity import Activity
from ecapture import ecapture as ec
import numpy

ec.capture(1, False, "test.jpg")
image = face_recognition.load_image_file("test.jpg")

encoding = numpy.fromstring(face_recognition.face_encodings(image)[0].tostring())

result = face_recognition.compare_faces([encoding], encoding)
print(result)