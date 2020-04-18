from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk

import face_recognition
import numpy

from FaceIdentification import FaceIdentification
from Administrator import Administrator
from Member import Member
from pymongo import MongoClient
from ecapture import ecapture as ec

import pymongo
from DBController import DBController
from Activity import Activity
from datetime import datetime

ha = face_recognition.load_image_file("ha.png")
y_ha = face_recognition.load_image_file("y_ha.png")
enha = face_recognition.face_encodings(ha)[0]
en_yha = face_recognition.face_encodings(y_ha)[0]
trump = face_recognition.load_image_file("trump.png")
ent = face_recognition.face_encodings(trump)[0]

list = []

list.append(enha)
list.append(en_yha)
list.append(ent)

result = face_recognition.compare_faces(list, enha)
print(result)