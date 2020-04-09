from FaceIdentification import FaceIdentification
import face_recognition
from ecapture import ecapture as ec

test = FaceIdentification()

ec.capture(1, False,"test.jpg")
print(test.set_face_id("abc"))
image = face_recognition.load_image_file("test.jpg")

result = test.compare_to(image)
print(result)