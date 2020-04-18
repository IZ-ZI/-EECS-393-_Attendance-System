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

screen = None
joinedActivityBox = None
joinedFrame = None
joinedScroll = None
login_account_entry = None
login_password_entry = None
login_account = None
login_password = None

member_id_entry = None
member_name_entry = None
member_email_entry = None
member_password_entry = None
member_confirm_password_entry = None
member_apply_club_id_entry = None

member_id = None
member_name = None
member_email = None
member_password = None
member_confirm_password = None
member_apply_club_id = None
member_register_feedback = None

new_date = None
new_start_time = None
new_end_time = None
new_location = None

screenAdmin = None
activityBox = None

new_club_id = None

activity_name = None
activity_date = None
activity_start_time = None
activity_end_time = None
activity_id = None
activity_location = None
screen1 = None
screenMember = None
club_register_feedback = None

club_id = None
club_name = None
club_email = None
club_password = None
club_confirm_password = None

club_id_entry = None
club_name_entry = None
club_email_entry = None
club_password_entry = None
club_confirm_password_entry = None


currentMemberBox = None
currentScroll = None
currentFrame = None
buttonFrameC = None

pendingMemberBox = None
pendingFrame = None
pendingScroll = None
buttonFrameP = None

clubBox = None
clubScroll = None
clubFrame = None

show_password = None

camSelected = None
frameimg = None
capture = None
file = None

yearOption = ["2020", "2021"]
monthOption = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

dayOption = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,32):
    dayOption.append(str(i))
hourOption = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10, 25):
    hourOption.append(str(i))
minuteOption = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10, 61):
    minuteOption.append(str(i))


cluster = MongoClient(
    "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
    "=majority")
db = cluster["AMS"]
collection_member = db["Member"]
collection_admin = db["Administrator"]
collection_activity = db["Activity"]

db_controller = DBController(collection_member, collection_admin, collection_activity)


def main_screen():
    global screen

    screen = Tk()
    screen.geometry("600x300")
    screen.title("Attendance System Login")
    # screen.configure(background='turquoise')

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    xCoor = screen_width / 2
    yCoor = screen_height / 2

    screen.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))

    global login_page
    login_page = Frame(screen, width=screen_width, height=screen_height)
    login_page.grid(row=0, column=0)

    global login_account_entry
    global login_password_entry
    global login_account
    global login_password
    global show_password

    login_account = StringVar()
    login_password = StringVar()

    Label(login_page, text="Club/Organization ID", font=("new roman", 21)).place(x=screen_width / 24,
                                                                                 y=screen_height * 2 / 30)

    # member_email_entry = Entry(screen1, textvariable=member_email)

    login_account_entry = Entry(login_page, textvariable=login_account, width="30")
    login_account_entry.place(x=screen_width / 24, y=screen_height * 5 / 30)

    Label(login_page, text="Password", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height * 10 / 30)
    show_password = BooleanVar()
    Checkbutton(login_page, text="show password", variable=show_password, command=display_password).place(
        x=screen_width / 24, y=screen_height * 15 / 30)
    login_password_entry = Entry(login_page, show='*', textvariable=login_password, width="30")
    login_password_entry.place(x=screen_width / 24, y=screen_height * 13 / 30)

    # highlightbackground = 'green'

    Button(login_page, text="Administrator", font=("new roman", 15), height="5", width="20", command=admin,
           fg='black').place(
        x=screen_width * 6.5 / 10, y=screen_height / 25)
    Button(login_page, text="Member", font=("new roman", 15), height="5", width="20", command=member,
           fg='black', ).place(x=screen_width * 6.5 / 10,
                               y=screen_height / 4 + screen_height / 30)

    Button(login_page, text="Administrator Login", font=("new roman", 15), height="5", width="20", command=admin_login,
           fg='black').place(
        x=screen_width / 30,
        y=screen_height * 2 / 3)
    # Button(screen, text="Login", height= "3", width = "20", command = login, fg='black').grid(row=6, column=0)
    Button(login_page, text="Forget/Reset Password", font=("new roman", 15), height="5", width="20", command=forget,
           fg='black').place(
        x=screen_width / 3 + screen_width / 30, y=screen_height * 2 / 3)

    Button(login_page, text="New Club Register", font=("new roman", 15), height="5", width="20", command=club_register,
           fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)

    # global button
    # button = Button(screen,text='Submit',command=changeText)
    # button.pack()
    raise_frame(login_page)
    screen.mainloop()

def switch_camera(event=0, nextCam=-1):
    global camSelected, capture, file

    if nextCam == -1:
        camSelected += 1
    else:
        camIndex = nextCam
    del (capture)
    capture = cv2.VideoCapture(camIndex + cv2.CAP_DSHOW)

    # try to get a frame, if it returns nothing
    success, frame = capture.read()
    if not success:
        camIndex = 0
        del (capture)
        cap = cv2.VideoCapture(camIndex + cv2.CAP_DSHOW)

    f = open(file, 'w')
    f.write(str(camIndex))
    f.close()


def raise_frame(frame):
    frame.tkraise()
    screen.title("Attendance System Login")


def club_register_check():
    global db_controller
    if (club_password.get() != club_confirm_password.get()):
        club_register_feedback['text'] = 'Password difference'
        # club_register_feedback.set("Password Difference")
    elif (
            club_id.get() == '' or club_name.get() == '' or club_email.get() == '' or club_password.get() == '' or club_confirm_password.get() == ''):
        club_register_feedback['text'] = 'Please fill all the spaces'
    elif (
            db_controller.admin_is_present(club_id.get())):
        club_register_feedback['text'] = 'This id has already been registered'
    else:
        club_info()


def member_register_check():
    global db_controller
    if (member_password.get() != member_confirm_password.get()):
        member_register_feedback['text'] = 'Password difference'
    elif (
            member_id.get() == '' or member_name.get() == '' or member_email.get() == '' or member_password.get() == '' or member_confirm_password.get() == '' or member_apply_club_id.get() == ''):
        member_register_feedback['text'] = 'Please fill all the spaces'
    elif (
            db_controller.member_is_present(member_id.get())):
        member_register_feedback['text'] = 'User id has already been registered'
    elif (
            not db_controller.admin_is_present(member_apply_club_id.get())):
        member_register_feedback['text'] = 'Club id does not exist'
    else:
        member_info()


def club_info():
    # file = open(club_id.get() + ".txt", "w")
    # file.write(club_id.get() + "\n")
    # file.write(club_name.get() + "\n")
    # file.write(club_email.get() + "\n")
    # file.write(club_password.get() + "\n")
    # file.write(club_confirm_password.get() + "\n")
    # file.close()
    global db_controller

    administrator = Administrator(club_name.get(), club_id.get(), club_email.get(), club_password.get())
    db_controller.add_admin(administrator)

    club_id_entry.delete(0, END)
    club_name_entry.delete(0, END)
    club_email_entry.delete(0, END)
    club_password_entry.delete(0, END)
    club_confirm_password_entry.delete(0, END)

    club_register_feedback['text'] = 'Registration Success'


def member_info():
    # file = open(member_id.get() + ".txt", "w")
    # file.write(member_id.get() + "\n")
    # file.write(member_name.get() + "\n")
    # file.write(member_email.get() + "\n")
    # file.write(member_password.get() + "\n")
    # file.write(member_confirm_password.get() + "\n")
    # file.write(member_apply_club_id.get() + "\n")
    # file.close()
    global db_controller

    new_member = Member(member_name.get(), member_id.get(), member_email.get(), member_password.get())
    db_controller.add_member(new_member)
    print(db_controller.retrieve_admin(member_apply_club_id.get())["email_address"])
    admin_email = db_controller.retrieve_admin(member_apply_club_id.get())["email_address"]
    member_register_feedback['text'] = 'Registration Success'
    db_controller.request_permission(member_apply_club_id.get(), new_member.get_id(), admin_email,
                                     new_member.get_name())

    member_id_entry.delete(0, END)
    member_name_entry.delete(0, END)
    member_email_entry.delete(0, END)
    member_password_entry.delete(0, END)
    member_confirm_password_entry.delete(0, END)
    member_apply_club_id_entry.delete(0, END)


def member_register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("New Member Registration")
    screen1.geometry("600x570")

    global member_id
    global member_name
    global member_email
    global member_password
    global member_confirm_password
    global member_apply_club_id

    global member_id_entry
    global member_name_entry
    global member_email_entry
    global member_password_entry
    global member_confirm_password_entry
    global member_apply_club_id_entry
    global member_register_feedback

    member_id = StringVar()
    member_name = StringVar()
    member_email = StringVar()
    member_password = StringVar()
    member_confirm_password = StringVar()
    member_apply_club_id = StringVar()

    # 1
    Label(screen1, text="").pack()
    Label(screen1, text="User ID").pack()
    member_id_entry = Entry(screen1, textvariable=member_id)
    member_id_entry.pack()
    # 2
    Label(screen1, text="").pack()
    Label(screen1, text="Name").pack()
    member_name_entry = Entry(screen1, textvariable=member_name)
    member_name_entry.pack()
    # 3
    Label(screen1, text="").pack()
    Label(screen1, text="Email").pack()
    member_email_entry = Entry(screen1, textvariable=member_email)
    member_email_entry.pack()
    # 4
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    member_password_entry = Entry(screen1, show='*', textvariable=member_password)
    member_password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    member_confirm_password_entry = Entry(screen1, show='*', textvariable=member_confirm_password)
    member_confirm_password_entry.pack()
    # 6
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization ID").pack()
    member_apply_club_id_entry = Entry(screen1, textvariable=member_apply_club_id)
    member_apply_club_id_entry.pack()
    # 7
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="20", command=member_register_check).pack()

    # 8
    Label(screen1, text="").pack()
    member_register_feedback = Label(screen1, text=" ", fg="green", font=("new roman", 15))
    member_register_feedback.pack()


def club_register():
    global screen1
    global club_register_feedback

    screen1 = Toplevel(screen)
    screen1.title("New Club Registration")
    screen1.geometry("600x570")

    global club_id
    global club_name
    global club_email
    global club_password
    global club_confirm_password

    club_id = StringVar()
    club_name = StringVar()
    club_email = StringVar()
    club_password = StringVar()
    club_confirm_password = StringVar()

    global club_id_entry
    global club_name_entry
    global club_email_entry
    global club_password_entry
    global club_confirm_password_entry

    # 1
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization ID").pack()
    club_id_entry = Entry(screen1, textvariable=club_id)
    club_id_entry.pack()

    # 2
    Label(screen1, text="").pack()
    Label(screen1, text="Name of the Club/Organization").pack()
    club_name_entry = Entry(screen1, textvariable=club_name)
    club_name_entry.pack()
    # 3
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization Email").pack()
    club_email_entry = Entry(screen1, textvariable=club_email)
    club_email_entry.pack()
    # 4
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    club_password_entry = Entry(screen1, show='*', textvariable=club_password)
    club_password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    club_confirm_password_entry = Entry(screen1, show='*', textvariable=club_confirm_password)
    club_confirm_password_entry.pack()

    # 6
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="20", command=club_register_check).pack()

    # 7
    Label(screen1, text="").pack()
    club_register_feedback = Label(screen1, text=" ", fg="green", font=("new roman", 15))
    club_register_feedback.pack()


def admin():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="Club/Organization ID", font=("new roman", 21)).place(x=screen_width / 24,
                                                                             y=screen_height * 2 / 30)
    Button(screen, text="New Club Register", font=("new roman", 15), height="5", width="20", command=club_register,
           fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Administrator Login", font=("new roman", 15), height="5", width="20", command=admin_login,
           fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)


def clubList(logged_member_id):
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    frame = Frame(screenMember, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height - 27)

    global clubBox
    Label(frame, text="Clubs", font=("new roman", 21)).pack()
    clubFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
    clubScroll = Scrollbar(clubFrame)
    clubScroll.pack(side=RIGHT, fill=Y)
    clubBox = Listbox(clubFrame, yscrollcommand=clubScroll.set, width=int(screen_width / 8), height=19,
                      selectmode=SINGLE)

    show_club_list(logged_member_id)

    clubBox.pack(side=LEFT)
    clubScroll.config(command=clubBox.yview)
    clubFrame.pack()

    buttonFrameC = Frame(frame, padx=1, pady=3)
    Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=9,
           command=lambda: refreshClub(logged_member_id)).grid(row=0,
                                                               column=0)
    Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=7,
           command=lambda: viewClub(logged_member_id)).grid(row=0, column=1)
    Button(buttonFrameC, text="Apply New", font=("new roman", 18), height=1, width=9,
           command=lambda: applyClub(logged_member_id)).grid(row=0,
                                                             column=2)
    buttonFrameC.pack()

    bottomFrame = Frame(screenMember, padx=10, pady=5)
    bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5, height=int(screen_height * 2 / 3 - 10))


def applyClub(logged_member_id):
    global new_club_id
    global applyClubScreen
    global apply_club_feedback
    new_club_id = StringVar()
    applyClubScreen = Toplevel(screen)
    applyClubScreen.geometry("300x200+30+30")
    applyClubScreen.title("Apply for New Club")
    Label(applyClubScreen, text="").pack()
    Label(applyClubScreen, text="Club ID", font=("new roman", 18)).pack()
    clubID_entry = Entry(applyClubScreen, textvariable=new_club_id)
    clubID_entry.pack()
    Label(applyClubScreen, text="").pack()
    Button(applyClubScreen, text="Apply", width=20, height=2, command=lambda: submitClubID(logged_member_id)).pack()
    apply_club_feedback = Label(applyClubScreen, text=" ", fg="green", font=("new roman", 15))
    apply_club_feedback.pack()

def submitClubID(logged_member_id):
    if db_controller.admin_is_present(new_club_id.get()):
        db_controller.add_member_to_pending_members(new_club_id.get(), logged_member_id)
        apply_club_feedback['text'] = 'Apply Success'
    else:
        apply_club_feedback['text'] = 'Club not exists'


def member_login():
    global screenMember
    print("member login session started")
    print('%s' % login_account_entry)
    # implement whatever needed to check for login
    logged_member_curse = db_controller.retrieve_member(login_account.get())
    if not db_controller.member_login(login_account.get(), login_password.get()):
        print('error')
        screenMember = Toplevel(screen)
        screenMember.title("Error")
        screen_width = screen.winfo_screenwidth() / 4
        screen_height = screen.winfo_screenheight() / 4
        xCoor = screen_width / 2 + 20
        yCoor = screen_height / 2 + 20

        screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))
    else:
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        xCoor = screen_width / 2 + 20
        yCoor = screen_height / 2 + 20

        screenMember = Frame(screen, width=screen_width, height=screen_height)
        screenMember.grid(row=0, column=0)
        screen.title("Member: %s" % logged_member_curse["name"])

        Button(screenMember, text="Log out", font=("new roman", 13), command=lambda: raise_frame(login_page)).place(
            x=screen_width - 70, y=screen_height - 25)

        Button(screenMember, text="Set Face ID", font=("new roman", 13), width=10,
               command=lambda: setFaceID(logged_member_curse["_id"])).place(x=screen_width / 2 + 10,
                                                                            y=screen_height - 25)

        leftFrame = Frame(screenMember, padx=10, pady=10)
        leftFrame.place(x=0, y=2, width=screen_width / 2, height=screen_height / 3)
        Button(leftFrame, text="My Clubs", font=("new roman", 20), height=2, width=25,
               command=lambda: clubList(logged_member_curse["_id"])).grid(row=0,
                                                                          column=0)
        Label(leftFrame, text="", height=1, width=25).grid(row=1, column=0)
        Button(leftFrame, text="My Activities", font=("new roman", 20), height=2, width=25,
               command=lambda: activityList(logged_member_curse["_id"])).grid(
            row=2, column=0)

        frame = Frame(screenMember, padx=10, pady=10)
        frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height - 27)

        clubList(logged_member_curse["_id"])


def render_PIP(content_frame, camindex):
    global capture

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    capture.release()
    capture = cv2.VideoCapture(camindex + cv2.CAP_DSHOW)
    _, frame = capture.read()
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 3)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width / 2)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, int(screen_height * 2 / 3))
    picture = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    frameimg = Image.fromarray(picture)
    imgtk = ImageTk.PhotoImage(image=frameimg)
    content_frame.imgtk = imgtk
    content_frame.configure(image=imgtk)

    content_frame.after(10, render_PIP, content_frame, camindex)

def setFaceID(logged_member_id):
    global file, screenSetfaceID, frameimg, capture
    camIndex = 1
    # try:
    #     f = open(file, 'r')
    #     camIndex = int(f.readline())
    # except:
    #     camIndex = 0

    capture = cv2.VideoCapture(camIndex + cv2.CAP_DSHOW)
    success, frame = capture.read()
    if not success:
        if camIndex == 0:
            print("Camera not detected 1. Check connection.")
            sys.exit(1)
        else:
            switch_camera(nextCam=1)
            success, frame = capture.read()
            if not success:
                print("Camera not detected. Check connection.")
                sys.exit(1)

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    screenSetfaceID = Toplevel(screen)
    screenSetfaceID.title("Set Face ID")
    screenSetfaceID.geometry("%dx%d" % (screen_height, screen_height))
    Label(screenSetfaceID, text="").pack()
    # Label(screenSetfaceID, text="").pack()
    Button(screenSetfaceID, text="Take Face ID Photo", height=3, width=20,
           command=lambda: takeFaceIDPhoto(logged_member_id)).pack()
    photoFrame = Label(screenSetfaceID, padx=10, pady=10, width=int(screen_height * 2 / 3),
                            height=int(screen_height * 2 / 3))
    photoFrame.pack()
    render_PIP(photoFrame,camIndex)
    capture.release()


def takeFaceIDPhoto(logged_member_id):
    global capture

    _, face_photo = capture.read()
    photo = cv2.imwrite('face.png', face_photo)
    # conditional statement needed
    encoding = ""
    print("take face id photo")
    #photo = ec.capture(1, False, "your photo.jpg")

    fr_photo = face_recognition.load_image_file("face.png")
    face_id = FaceIdentification.encoding_from_photo(fr_photo)
    db_controller.update_member_face_id(logged_member_id, face_id)
    try:
        encoding = numpy.fromstring(db_controller.retrieve_member_face_id(logged_member_id))
    except:
        setIDFail()
        encoding = None
    if FaceIdentification.compare_to(encoding, encoding):
        setIDSuccess()
    else:
        setIDFail()


def setIDSuccess():
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenSetfaceID)
    Label(frame, text="Success", fg='green').pack()
    frame.place(x=0, y=screen_height - 50, width=screen_height)


def setIDFail():
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenSetfaceID)
    Label(frame, text="Failed, Please Try Again.", fg='red').pack()
    frame.place(x=0, y=screen_height - 50, width=screen_height)


def viewClub(logged_member_id):
    if clubBox.curselection() != ():
        clicked_item_index = clubBox.curselection()[0]
        view_club_id = db_controller.clubs_member_added(logged_member_id)[clicked_item_index]
        view_club_curse = db_controller.retrieve_admin(view_club_id)
        print("view club info and my status")
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        bottomFrame = LabelFrame(screenMember, padx=10, pady=5)
        bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5,
                          height=int(screen_height * 2 / 3 - 10))
        Label(bottomFrame, text="Club Status", font=("new roman", 15)).pack()

        clubInfoFrame = Frame(bottomFrame, padx=1, pady=3)
        Label(clubInfoFrame, text="Club Name:", font=("new roman", 13)).grid(row=0, column=0, sticky=W)
        Label(clubInfoFrame, text=view_club_curse["name"]).grid(row=0, column=1, sticky=W)
        Label(clubInfoFrame, text="Club ID: ", font=("new roman", 13)).grid(row=1, column=0, sticky=W)
        Label(clubInfoFrame, text=view_club_curse["_id"], font=("new roman", 13)).grid(row=1, column=1, sticky=W)
        Label(clubInfoFrame, text="Total Number of Events:     ").grid(row=2, column=0, sticky=W)
        Label(clubInfoFrame, text=len(view_club_curse["activities"]), font=("new roman", 13)).grid(row=2, column=1,
                                                                                                   sticky=W)
        Label(clubInfoFrame, text="My Absenses", font=("new roman", 13)).grid(row=3, column=0, sticky=W)
        Label(clubInfoFrame, text="3", font=("new roman", 13)).grid(row=3, column=1, sticky=W)
        Label(clubInfoFrame, text="Attendance Rate", font=("new roman", 13)).grid(row=4, column=0, sticky=W)
        Label(clubInfoFrame, text="80", font=("new roman", 13)).grid(row=4, column=1, sticky=W)
        clubInfoFrame.pack()

        '''global clubActivityBox
        clubActivityFrame = Frame(bottomFrame, padx=3, pady=3, height=int(screen_height / 6))
        Label(clubActivityFrame, text="My Events", font=("new roman", 13)).pack()
        clubActivityScroll = Scrollbar(clubActivityFrame)
        clubActivityScroll.pack(side=RIGHT, fill=Y)
        clubActivityBox = Listbox(clubActivityFrame, yscrollcommand=clubActivityScroll.set,
                                  width=int(screen_width / 2 - 7),
                                  height=4, selectmode=SINGLE)

        for i in range(1, 15):
            clubActivityBox.insert(END, "LINE" + str(i))

        clubActivityBox.pack(side=LEFT)
        clubActivityScroll.config(command=clubActivityBox.yview)
        clubActivityFrame.pack()
        Button(bottomFrame, text="View Activity Status", font=("new roman", 12), command=viewActivityStatus).pack()'''


def viewActivityStatus(logged_member_id):
    if myActivityBox.curselection() != ():
        clicked_item_index = myActivityBox.curselection()[0]
        view_activity_id = db_controller.member_activities(logged_member_id)[clicked_item_index]
        view_activity_curse = db_controller.retrieve_activity(view_activity_id)
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        bottomFrame = LabelFrame(screenMember, padx=10, pady=5)
        bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5,
                          height=int(screen_height * 2 / 3 - 10))
        Label(bottomFrame, text="Activity Status", font=("new roman", 15)).pack()

        activityInfoFrame = Frame(bottomFrame, padx=1, pady=3)
        Label(activityInfoFrame, text="Club Name:", font=("new roman", 13)).grid(row=0, column=0, sticky=W)
        Label(activityInfoFrame, text=view_activity_curse["admin"]).grid(row=0, column=1, sticky=W)
        Label(activityInfoFrame, text="Activity Name:", font=("new roman", 13)).grid(row=1, column=0, sticky=W)
        Label(activityInfoFrame, text=view_activity_curse["name"], font=("new roman", 13)).grid(row=1, column=1,
                                                                                                sticky=W)
        Label(activityInfoFrame, text="Start Time: ", font=("new roman", 13)).grid(row=2, column=0, sticky=W)
        Label(activityInfoFrame, text=view_activity_curse["start_time"], font=("new roman", 13)).grid(row=2, column=1,
                                                                                                      sticky=W)
        Label(activityInfoFrame, text="End Time: ", font=("new roman", 13)).grid(row=3, column=0, sticky=W)
        Label(activityInfoFrame, text=view_activity_curse["end_time"], font=("new roman", 13)).grid(row=3, column=1,
                                                                                                    sticky=W)
        Label(activityInfoFrame, text="Present?", font=("new roman", 13)).grid(row=4, column=0, sticky=W)
        Label(activityInfoFrame,
              text=db_controller.member_status_in_activity(logged_member_id, view_activity_curse["admin"],
                                                          view_activity_id), font=("new roman", 13)).grid(row=4,
                                                                                                          column=1,
                                                                                                          sticky=W)

        activityInfoFrame.pack()


def deleteClub():
    clicked_items = clubBox.curselection()
    clubBox.delete(clicked_items)
    print("leave club")


def activityList(logged_member_id):

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    frame = Frame(screenMember, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height - 27)

    global myActivityBox
    Label(frame, text="Activities", font=("new roman", 21)).pack()
    myActivityFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
    myActivityScroll = Scrollbar(myActivityFrame)
    myActivityScroll.pack(side=RIGHT, fill=Y)
    myActivityBox = Listbox(myActivityFrame, yscrollcommand=myActivityScroll.set, width=int(screen_width / 8),
                            height=19, selectmode=SINGLE)

    show_my_activities(logged_member_id)

    myActivityBox.pack(side=LEFT)
    myActivityScroll.config(command=myActivityBox.yview)
    myActivityFrame.pack()

    buttonFrame = Frame(frame, padx=2, pady=3)
    Button(buttonFrame, text="Refresh", font=("new roman", 18), height=1, width=13,
           command=lambda: refreshMyActivity(logged_member_id)).grid(
        row=0, column=0)
    Label(buttonFrame, text=" ").grid(row=0, column=1)
    Button(buttonFrame, text="View", font=("new roman", 18), height=1, width=13,
           command=lambda: viewActivityStatus(logged_member_id)).grid(
        row=0, column=2)
    buttonFrame.pack()

    bottomFrame = Frame(screenMember, padx=10, pady=5)
    bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5, height=int(screen_height * 2 / 3 - 10))


def isUpdated(activity_in_list, activity_from_db):
    if activity_in_list["_id"] == activity_from_db["_id"]:
        return activity_in_list["start_time"] is not activity_from_db["start_time"] or activity_in_list[
            "end_time"] is not activity_from_db["end_time"] or activity_in_list["location"] is not activity_from_db[
                   "location"]


def show_my_activities(logged_member_id):
    global myActivityBox
    myActivityBox.delete(0, tk.END)
    for i in db_controller.member_activities(logged_member_id):
        activity_curse = db_controller.retrieve_activity(i)
        myActivityBox.insert(END, "ID: " + activity_curse["_id"] + "  "
                                 + "Name: " + activity_curse["name"] + "  "
                                 + "Location: " + activity_curse["location"])


def refreshMyActivity(logged_member_id):
    show_my_activities(logged_member_id)


def show_club_list(logged_member_id):
    global clubBox
    clubBox.delete(0, tk.END)
    for i in db_controller.clubs_member_added(logged_member_id):
        club_curse = db_controller.retrieve_admin(i)
        clubBox.insert(END, "ID: " + club_curse["_id"] + "  " + "Name: " + club_curse["name"])


def refreshClub(logged_member_id):
    show_club_list(logged_member_id)


def memberManagement(logged_admin_id):

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    frame = Frame(screenAdmin, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height - 27)

    Label(frame, text="Current Members", font=("new roman", 21)).pack()

    global currentMemberBox
    global currentScroll
    global currentFrame
    currentFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
    currentScroll = Scrollbar(currentFrame)
    currentScroll.pack(side=RIGHT, fill=Y)
    currentMemberBox = Listbox(currentFrame, yscrollcommand=currentScroll.set, width=int(screen_width / 8),
                               height=7, selectmode=SINGLE)
    showCurrentMember(logged_admin_id)

    currentMemberBox.pack(side=LEFT)
    currentScroll.config(command=currentMemberBox.yview)
    currentFrame.pack()

    buttonFrameC = Frame(frame, padx=1, pady=3)
    Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=9,
           command=lambda: refreshMember(logged_admin_id)).grid(
        row=0, column=0)

    Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=9,
           command=lambda: viewMember(logged_admin_id)).grid(row=0, column=1)

    Button(buttonFrameC, text="Delete", font=("new roman", 18), height=1, width=9,
           command=lambda: deleteMember(logged_admin_id)).grid(
        row=0, column=2)
    buttonFrameC.pack()

    Label(frame, text="", font=10).pack()
    Label(frame, text="Pending Members", font=("new roman", 21)).pack()

    global pendingFrame
    global pendingScroll
    global pendingFrame
    pendingFrame = Frame(frame, padx=1, pady=3)
    pendingScroll = Scrollbar(pendingFrame)
    pendingScroll.pack(side=RIGHT, fill=Y)
    global pendingMemberBox
    pendingMemberBox = Listbox(pendingFrame, yscrollcommand=pendingScroll.set, width=int(screen_width / 8),
                               height=7, selectmode=SINGLE)
    pendingMemberBox.pack(side=LEFT)
    pendingScroll.config(command=pendingMemberBox.yview)
    pendingFrame.pack()

    buttonFrameP = Frame(frame, padx=1, pady=3)
    Button(buttonFrameP, text="Refresh", font=("new roman", 18), height=1, width=9,
           command=lambda: refreshList(logged_admin_id)).grid(row=0,
                                                              column=0)
    Button(buttonFrameP, text="Accept", font=("new roman", 18), height=1, width=9,
           command=lambda: acceptMember(logged_admin_id)).grid(row=0,
                                                               column=1)
    Button(buttonFrameP, text="Reject", font=("new roman", 18), height=1, width=9,
           command=lambda: rejectMember(logged_admin_id)).grid(row=0,
                                                               column=2)
    buttonFrameP.pack()

    bottomFrame = Frame(screenAdmin, padx=10, pady=5)
    bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5, height=int(screen_height * 2 / 3 - 10))

    showPendingMember(logged_admin_id)


def activityManagement(logged_admin_id):
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenAdmin, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height - 27)
    Label(frame, text="Activities", font=("new roman", 21)).pack()

    global activityBox
    activityFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 2))
    activityScroll = Scrollbar(activityFrame)
    activityScroll.pack(side=RIGHT, fill=Y)
    activityBox = Listbox(activityFrame, yscrollcommand=activityScroll.set, width=int(screen_width / 8), height=19,
                          selectmode=SINGLE)

    show_admin_activities(logged_admin_id)

    activityBox.pack(side=LEFT)
    activityScroll.config(command=activityBox.yview)
    activityFrame.pack()

    buttonFrameA = Frame(frame, padx=0, pady=3)
    Button(buttonFrameA, text="Refresh", font=("new roman", 18), height=1, width=7,
           command=lambda: refreshActivity(logged_admin_id)).grid(row=0, column=0)
    Button(buttonFrameA, text="View", font=("new roman", 18), height=1, width=6,
           command=lambda: viewActivity(logged_admin_id)).grid(row=0, column=1)
    Button(buttonFrameA, text="Create", font=("new roman", 18), height=1, width=7,
           command=lambda: createActivity(logged_admin_id)).grid(row=0, column=2)
    Button(buttonFrameA, text="Delete", font=("new roman", 18), height=1, width=7,
           command=lambda: deleteActivity(logged_admin_id)).grid(row=0, column=3)
    buttonFrameA.pack()

    bottomFrame = Frame(screenAdmin, padx=10, pady=5)
    bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5, height=int(screen_height * 2 / 3 - 10))


def show_admin_activities(logged_admin_id):
    global activityBox
    activityBox.delete(0, tk.END)
    for i in db_controller.admin_activities(logged_admin_id):
        activity_curse = db_controller.retrieve_activity(i)
        activityBox.insert(END, "ID: " + activity_curse["_id"] + "  "
                               + "Name: " + activity_curse["name"] + "  "
                               + "Location: " + activity_curse["location"])


def refreshActivity(logged_admin_id):
    show_admin_activities(logged_admin_id)


def deleteActivity(logged_admin_id):
    if activityBox.curselection() != ():
        clicked_item_index = activityBox.curselection()[0]
        del_activity_id = db_controller.admin_activities(logged_admin_id)[clicked_item_index]
        db_controller.remove_activity_from_admin(del_activity_id, logged_admin_id)
        for i in db_controller.added_members(logged_admin_id):
            db_controller.remove_activity_from_member(logged_admin_id, del_activity_id, i)
        db_controller.delete_activity(del_activity_id)
        activityBox.delete(clicked_item_index)


def updateTime(logged_admin_id, clicked_item_index, activity_id, activity_name):
    print("update time")
    global updateTimeScreen
    global new_date
    global new_start_time
    global new_end_time
    global new_location
    global update_activity_feedback

    new_date = StringVar()
    new_start_time = StringVar()
    new_end_time = StringVar()
    new_location = StringVar()

    updateTimeScreen = Toplevel(screen)
    updateTimeScreen.title("Update Activity Information")
    updateTimeScreen.geometry("400x400+30+30")
    Label(updateTimeScreen, text="").pack()
    Label(updateTimeScreen, text="New Date", font=("new roman", 15)).pack()
    dateFrame = Frame(updateTimeScreen)
    Label(dateFrame, text = "Year").grid(row = 0, column = 0)
    Label(dateFrame, text = "Month").grid(row = 0, column = 1)
    Label(dateFrame, text = "Day").grid(row = 0, column = 2)
    global yearClickedUpdate
    yearClickedUpdate = StringVar()
    yearClickedUpdate.set(yearOption[0])
    global monthClickedUpdate
    monthClickedUpdate = StringVar()
    monthClickedUpdate.set(monthOption[0])
    global dayClickedUpdate
    dayClickedUpdate = StringVar()
    dayClickedUpdate.set(dayOption[0])

    yearDrop = OptionMenu(dateFrame, yearClickedUpdate, *yearOption)
    yearDrop.grid(row = 1, column = 0)
    monthDrop = OptionMenu(dateFrame, monthClickedUpdate, *monthOption)
    monthDrop.grid(row = 1, column = 1)
    dayDrop = OptionMenu(dateFrame, dayClickedUpdate, *dayOption)
    dayDrop.grid(row = 1, column = 2)
    dateFrame.pack()

    Label(updateTimeScreen, text="").pack()
    Label(updateTimeScreen, text = "New Start Time", font = ("new roman", 15)).pack()
    startTimeFrame = Frame(updateTimeScreen)
    Label(startTimeFrame, text = "Hour").grid(row = 0, column = 0)
    Label(startTimeFrame, text = "").grid(row = 0, column = 1)
    Label(startTimeFrame, text = "Minute").grid(row = 0, column = 2)
    global hourClickedStartUpdate
    hourClickedStartUpdate = StringVar()
    hourClickedStartUpdate.set(hourOption[0])
    global minuteClickedStartUpdate
    minuteClickedStartUpdate= StringVar()
    minuteClickedStartUpdate.set(minuteOption[0])

    hourDropStart = OptionMenu(startTimeFrame, hourClickedStartUpdate, *hourOption)
    hourDropStart.grid(row = 1, column = 0)
    minuteDropStart = OptionMenu(startTimeFrame, minuteClickedStartUpdate, *minuteOption)
    minuteDropStart.grid(row = 1, column = 2)
    startTimeFrame.pack()

    Label(updateTimeScreen, text="").pack()
    Label(updateTimeScreen, text = "New End Time", font = ("new roman", 15)).pack()
    endTimeFrame = Frame(updateTimeScreen)
    Label(endTimeFrame, text = "Hour").grid(row = 0, column = 0)
    Label(endTimeFrame, text = "").grid(row = 0, column = 1)
    Label(endTimeFrame, text = "Minute").grid(row = 0, column = 2)
    global hourClickedEndUpdate
    hourClickedEndUpdate = StringVar()
    hourClickedEndUpdate.set(hourOption[0])
    global minuteClickedEndUpdate
    minuteClickedEndUpdate= StringVar()
    minuteClickedEndUpdate.set(minuteOption[0])

    hourDropEnd = OptionMenu(endTimeFrame, hourClickedEndUpdate, *hourOption)
    hourDropEnd.grid(row = 1, column = 0)
    minuteDropEnd = OptionMenu(endTimeFrame, minuteClickedEndUpdate, *minuteOption)
    minuteDropEnd.grid(row = 1, column = 2)
    endTimeFrame.pack()

    Label(updateTimeScreen, text="").pack()
    Label(updateTimeScreen, text="New Location", font=("new roman", 15)).pack()
    location_entry = Entry(updateTimeScreen, textvariable=new_location)
    location_entry.pack()
    Label(updateTimeScreen, text="").pack()

    Button(updateTimeScreen, text="Update Information", font=("new roman", 15), height=2, width=20,
           command=lambda: updateTimeInfo(logged_admin_id, clicked_item_index, activity_id, activity_name)).pack()

    update_activity_feedback = Label(updateTimeScreen, text="", fg="green", font=("new roman", 15))
    update_activity_feedback.pack()


def updateTimeInfo(logged_admin_id, clicked_item_index, activity_id, activity_name):
    year = yearClickedUpdate.get()
    month = monthClickedUpdate.get()
    day = dayClickedUpdate.get()
    startHour = hourClickedStartUpdate.get()
    startMinute = minuteClickedStartUpdate.get()
    endHour = hourClickedEndUpdate.get()
    endMinute = minuteClickedEndUpdate.get()

    start_time_string = year + "-" + month + "-" + day + " " + startHour + ":" + startMinute + ":" + "00"
    end_time_string = year + "-" + month + "-" + day + " " + endHour + ":" + endMinute + ":" + "00"

    if(new_location.get()==''):
        update_activity_feedback['text'] = 'Enter new location please'
    else:
        activity = Activity(activity_id, activity_name, start_time_string, end_time_string,
                            new_location.get())
        db_controller.update_activity(activity)
        activityBox.delete(clicked_item_index)
        refreshActivity(logged_admin_id)
        update_activity_feedback['text'] = 'Update Success'


def refreshActivityInfo(logged_admin_id):
    viewActivity(logged_admin_id)


def viewActivity(logged_admin_id):
    if activityBox.curselection() != ():
        clicked_item_index = activityBox.curselection()[0]
        view_activity_id = db_controller.admin_activities(logged_admin_id)[clicked_item_index]
        view_activity_curse = db_controller.retrieve_activity(view_activity_id)
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        bottomFrame = LabelFrame(screenAdmin, padx=10, pady=5)
        bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5,
                          height=int(screen_height * 2 / 3 - 10))
        Label(bottomFrame, text="Activity Status", font=("new roman", 15)).pack()

        timeFrame = Frame(bottomFrame, padx=1, pady=3)
        Label(timeFrame, text="Start Time", font=("new roman", 13)).grid(row=0, column=0)
        Label(timeFrame, text="         ").grid(row=0, column=1)
        Label(timeFrame, text="End Time", font=("new roman", 13)).grid(row=0, column=2)
        # pull out information about the start time and end time
        Label(timeFrame, text=view_activity_curse["start_time"], font=("new roman", 13)).grid(row=1, column=0)
        Label(timeFrame, text="         ").grid(row=1, column=1)
        Label(timeFrame, text=view_activity_curse["end_time"], font=("new roman", 13)).grid(row=1, column=2)
        timeFrame.pack()

        buttonFrame = Frame(bottomFrame, padx=1, pady=2)
        Button(buttonFrame, text="Update Information", font=("new roman", 13), width=16, height=4,
               command=lambda: updateTime(logged_admin_id, clicked_item_index, view_activity_curse["_id"],
                                          view_activity_curse["name"])).grid(row=0,
                                                                             column=0)
        Button(buttonFrame, text="Refresh Information", font=("new roman", 13), width=16, height=4,
               command=lambda: refreshActivityInfo(logged_admin_id)).grid(row=0, column=1)
        buttonFrame.pack()

        Button(buttonFrame, text="Take Attendance", font=("new roman", 13), width=16, height=4,
               command=lambda: takeAttendance(logged_admin_id, view_activity_id)).grid(row=1, column=0)
        Button(buttonFrame, text="Change Status", font=("new roman", 13), width=16, height=4,
               command=memberStatusChange).grid(row=1, column=1)
        buttonFrame.pack()

def memberStatusChange():
    global statusUpdateScreen
    statusUpdateScreen = Toplevel(screen)
    statusUpdateScreen.title("Member Attendance Status Update")
    statusUpdateScreen.geometry("300x300+50+50")
    Label(statusUpdateScreen, text = "").pack()
    Label(statusUpdateScreen, text = "Activity ID", font = ("new roman", 15)).pack()
    Label(statusUpdateScreen, text = "123123").pack()
    Label(statusUpdateScreen, text="").pack()
    Label(statusUpdateScreen, text="Member ID", font = ("new roman", 15)).pack()
    update_entry = Entry(statusUpdateScreen)
    update_entry.pack()

    Label(statusUpdateScreen, text="").pack()
    Label(statusUpdateScreen, text="Update Status", font=("new roman", 15)).pack()
    options = ["On Time", "Late", "Absent"]
    global status_clicked
    status_clicked = StringVar()
    status_clicked.set(options[0])
    drop = OptionMenu(statusUpdateScreen, status_clicked, *options)
    drop.pack()

    Label(statusUpdateScreen, text="").pack()
    Button(statusUpdateScreen, text = "Update Attendance Status", font = ("new roman", 15), height = 2, command = updateStatus).pack()

def updateStatus():
    status = status_clicked.get()
    print(status)



def takeAttendancePicture(logged_admin_id, view_activity_id):
    global frameimg, capture, verify_attendance_feedback

    members_list = db_controller.added_members(logged_admin_id)
    members_faces = []
    members_names = []
    render_names = []
    for member in members_list:
        face = db_controller.retrieve_member_face_id(member)
        if not face == " ":
            members_faces.append(numpy.frombuffer(face))
            members_names.append(db_controller.retrieve_member_name(member))

    global capture

    _, face_photo = capture.read()
    photo = cv2.imwrite('pending.png', face_photo)
    # conditional statement needed
    encoding = ""
    print("take photo")
    #photo = ec.capture(1, False, "your photo.jpg")

    fr_photo = face_recognition.load_image_file("pending.png")
    face_encoding = face_recognition.face_encodings(fr_photo)[0]

    matches = face_recognition.compare_faces(members_faces, face_encoding)
    if True in matches:
        verify_attendance_feedback['text'] = 'Take Attendance Successfully'
        matched_face_index = matches.index(True)
        matched_member_id = members_list[matched_face_index]
        act_start = datetime.strptime(db_controller.activity_start_time(view_activity_id), '%m/%d/%y %H:%M:%S')
        act_end = datetime.strptime(db_controller.activity_end_time(view_activity_id), '%m/%d/%y %H:%M:%S')
        current_time = datetime.datetime.now()
        if current_time <= act_start:
            db_controller.set_member_activity_status(logged_admin_id, view_activity_id, matched_member_id, "On Time")
        elif current_time > act_start and current_time < act_end:
            db_controller.set_member_activity_status(logged_admin_id, view_activity_id, matched_member_id, "Late")
        else:
            db_controller.set_member_activity_status(logged_admin_id, view_activity_id, matched_member_id, "Absence")

    else:
        verify_attendance_feedback['text'] = 'Take Attendance Failed'



    # while True:
    #     _, frame = capture.read()
        # capture.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width / 2)
        # capture.set(cv2.CAP_PROP_FRAME_HEIGHT, int(screen_height * 2 / 3))
        # picture = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        #
        # frameimg = Image.fromarray(picture)
        # imgtk = ImageTk.PhotoImage(image=frameimg)
        # content_frame.imgtk = imgtk
        # content_frame.configure(image=imgtk)
        #content_frame.after(10, render_pip, content_frame)

        # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # rgb_small_frame = small_frame[:, :, ::-1]
        #
        # if process_this_frame:
        #     face_locations = face_recognition.face_locations(rgb_small_frame)
        #     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #
        #     render_names = []
        #     for face_encoding in face_encodings:
        #         matches = face_recognition.compare_faces(members_faces, face_encoding)
        #         name = "UNKNOWN"
        #
        #         face_distances = face_recognition.face_distance(members_faces, face_encoding)
        #         best_match_index = numpy.argmin(face_distances)
        #         if matches[best_match_index]:
        #             name = members_names[best_match_index]
        #
        #         render_names.append(name)
        # process_this_frame = not process_this_frame
        #
        # for (top, right, bottom, left, name) in zip(face_locations, members_names):
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0 , 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        # cv2.imshow('Taking Attendance', frame)
        # if cv2.waitKey(33) & 0xFF == 27:
        #     break


def takeAttendance(logged_admin_id, view_activity_id):
    global capture, file, screenAttendance, verify_attendance_feedback

    print("taking attendance")
    screenAttendance = Toplevel(screenAdmin)
    screenAttendance.title("Taking Attendance")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    screenAttendance.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))

    leftFrame = Frame(screenAttendance, padx=10, pady=10)
    leftFrame.place(x=0, y=2, width=screen_width / 2, height=int(screen_height * 2 / 3))
    Label(leftFrame, text="Member ID", font=("new roman", 15)).grid(row=0, column=0, sticky=W)
    memberid_entry = Entry(leftFrame, width=20)
    memberid_entry.grid(row=1, column=0)
    Button(leftFrame, text="OK", font=("new roman", 15), command=getMemberPhoto).grid(row=1, column=1)
    Label(leftFrame, text="").grid(row=2, column=0)
    Label(leftFrame, text="Photo on File", font=("new roman", 15)).grid(row=3, column=0, sticky=W)
    photoFrame = LabelFrame(leftFrame, padx=10, pady=10, width=screen_width / 4, height=screen_width / 4)
    photoFrame.grid(row=4, column=0)

    rightFrame = Frame(screenAttendance, padx=10, pady=10)
    rightFrame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=int(screen_height * 2 / 3))
    # try:
    #     f = open(file, 'r')
    #     camIndex = int(f.readline())
    # except:
    #     camIndex = 0
    camIndex = 1
    capture = cv2.VideoCapture(camIndex + cv2.CAP_DSHOW)
    success, frame = capture.read()
    # if not success:
    #     if camIndex == 0:
    #         print("Camera not detected. Check connection.")
    #         sys.exit(1)
    #     else:
    #         switch_camera(nextCam=0)
    #         success, frame = capture.read()
    #         if not success:
    #             print("Camera not detected. Check connection.")
    #             sys.exit(1)

    # Label(rightFrame, text="Camera", font=("new roman", 15)).grid(row=0, column=0, sticky=W)
    Button(rightFrame, text="Verify", font=("new roman", 15), height=2, width=20,
           command=lambda: takeAttendancePicture(logged_admin_id, view_activity_id)).pack()
    verify_attendance_feedback = Label(rightFrame, text="", fg="green", font=("new roman", 15))
    verify_attendance_feedback.pack()
    cameraframe = Label(rightFrame, padx=10, pady=10, width=int(screen_height * 2 / 3),
                            height=int(screen_height * 2 / 3))
    cameraframe.pack()
    render_PIP(cameraframe, camIndex)

    # Button(screenAttendance, text="Attend", font=("new roman", 15), height=2, width=20, command=attend).place(
    #     x=10, y=int(screen_height * 2 / 3) + 30)
    # Button(screenAttendance, text="Verify", font=("new roman", 15), height=2, width=20, command=takePhoto).place(
    #     x=screen_width / 2 + 10, y=int(screen_height * 2 / 3) + 30)


def takePhoto():
    ec.capture(1, False, "your photo.jpg")
    photo = face_recognition.load_image_file("your photo.jpg")

    print("take photo")


def attend():
    print("successfully take attendance")


def getMemberPhoto():
    print("get Member Photo")


def generateActivityReport():
    print("generating report")
    global screenReport
    screenReport = Toplevel(screen)
    screenReport.title("Activity Report")
    screenReport.geometry("300x300+50+50")
    Label(screenReport, text="").grid(row=0, column=0)
    Label(screenReport, text="Activity Name: ", font=("new roman", 15)).grid(row=1, column=0, sticky=W)
    Label(screenReport, text="Class 5", font=("new roman", 15)).grid(row=1, column=1, sticky=W)
    Label(screenReport, text="Number of Attendees:     ", font=("new roman", 15)).grid(row=2, column=0, sticky=W)
    Label(screenReport, text="30", font=("new roman", 15)).grid(row=2, column=1, sticky=W)
    Label(screenReport, text="Number of Attended: ", font=("new roman", 15)).grid(row=3, column=0, sticky=W)
    Label(screenReport, text="15", font=("new roman", 15)).grid(row=3, column=1, sticky=W)
    Label(screenReport, text="Number of Absenses: ", font=("new roman", 15)).grid(row=4, column=0, sticky=W)
    Label(screenReport, text="15", font=("new roman", 15)).grid(row=4, column=1, sticky=W)
    Label(screenReport, text="Attendance Rate", font=("new roman", 15)).grid(row=5, column=0, sticky=W)
    Label(screenReport, text="50", font=("new roman", 15)).grid(row=5, column=1, sticky=W)


def createActivity(logged_admin_id):
    global activity_name
    global activity_date
    global activity_start_time
    global activity_end_time
    global activity_id
    global activity_location
    global create_activity_feedback
    activity_name = StringVar()
    activity_date = StringVar()
    activity_start_time = StringVar()
    activity_end_time = StringVar()
    activity_id = StringVar()
    activity_location = StringVar()

    print("create activity")
    global screenCreateActivity
    screenCreateActivity = Toplevel(screenAdmin)
    screenCreateActivity.title("New Activity")
    screenCreateActivity.geometry("400x600+10+10")

    Label(screenCreateActivity, text="").pack()
    Label(screenCreateActivity, text="Activity ID").pack()
    id_entry = Entry(screenCreateActivity, textvariable=activity_id)
    id_entry.pack()

    # 1
    Label(screenCreateActivity, text="").pack()
    Label(screenCreateActivity, text="Activity Name").pack()
    activity_entry = Entry(screenCreateActivity, textvariable=activity_name)
    activity_entry.pack()
    # 2
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Date").pack()
    dateFrame = Frame(screenCreateActivity)
    Label(dateFrame, text = "Year").grid(row = 0, column = 0)
    Label(dateFrame, text = "Month").grid(row = 0, column = 1)
    Label(dateFrame, text = "Day").grid(row = 0, column = 2)
    global yearClickedCreate
    yearClickedCreate = StringVar()
    yearClickedCreate.set(yearOption[0])
    global monthClickedCreate
    monthClickedCreate = StringVar()
    monthClickedCreate.set(monthOption[0])
    global dayClickedCreate
    dayClickedCreate = StringVar()
    dayClickedCreate.set(dayOption[0])

    yearDrop = OptionMenu(dateFrame, yearClickedCreate, *yearOption)
    yearDrop.grid(row = 1, column = 0)
    monthDrop = OptionMenu(dateFrame, monthClickedCreate, *monthOption)
    monthDrop.grid(row = 1, column = 1)
    dayDrop = OptionMenu(dateFrame, dayClickedCreate, *dayOption)
    dayDrop.grid(row = 1, column = 2)
    dateFrame.pack()

    # 3
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Start Time").pack()
    startTimeFrame = Frame(screenCreateActivity)
    Label(startTimeFrame, text = "Hour").grid(row = 0, column = 0)
    Label(startTimeFrame, text = "").grid(row = 0, column = 1)
    Label(startTimeFrame, text = "Minute").grid(row = 0, column = 2)
    global hourClickedStart
    hourClickedStart = StringVar()
    hourClickedStart.set(hourOption[0])
    global minuteClickedStart
    minuteClickedStart= StringVar()
    minuteClickedStart.set(minuteOption[0])

    hourDropStart = OptionMenu(startTimeFrame, hourClickedStart, *hourOption)
    hourDropStart.grid(row = 1, column = 0)
    minuteDropStart = OptionMenu(startTimeFrame, minuteClickedStart, *minuteOption)
    minuteDropStart.grid(row = 1, column = 2)
    startTimeFrame.pack()

    # 4
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "End Time").pack()
    endTimeFrame = Frame(screenCreateActivity)
    Label(endTimeFrame, text = "Hour").grid(row = 0, column = 0)
    Label(endTimeFrame, text = "").grid(row = 0, column = 1)
    Label(endTimeFrame, text = "Minute").grid(row = 0, column = 2)
    global hourClickedEnd
    hourClickedEnd = StringVar()
    hourClickedEnd.set(hourOption[0])
    global minuteClickedEnd
    minuteClickedEnd= StringVar()
    minuteClickedEnd.set(minuteOption[0])

    hourDropEnd = OptionMenu(endTimeFrame, hourClickedEnd, *hourOption)
    hourDropEnd.grid(row = 1, column = 0)
    minuteDropEnd = OptionMenu(endTimeFrame, minuteClickedEnd, *minuteOption)
    minuteDropEnd.grid(row = 1, column = 2)
    endTimeFrame.pack()

    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Location").pack()
    location_entry = Entry(screenCreateActivity, textvariable=activity_location)
    location_entry.pack()

    Button(screenCreateActivity, text="Create Activity", height=3, width=20,
           command=lambda: activity_create_check(logged_admin_id)).pack()

    create_activity_feedback = Label(screenCreateActivity, text=" ", fg="green", font=("new roman", 15))
    create_activity_feedback.pack()


def activity_create_check(logged_admin_id):
    global db_controller
    if db_controller.activity_is_present(activity_id.get()):
        create_activity_feedback['text'] = 'ID has already been registered'
    else:
        newActivity(logged_admin_id)
        create_activity_feedback['text'] ='Create Success'


def newActivity(logged_admin_id):
    year = yearClickedCreate.get()
    month = monthClickedCreate.get()
    day = dayClickedCreate.get()
    startHour = hourClickedStart.get()
    startMinute = minuteClickedStart.get()
    endHour = hourClickedEnd.get()
    endMinute = minuteClickedEnd.get()

    start_time_string = year + "-" + month + "-" + day + " " + startHour + ":" + startMinute + ":" + "00"
    end_time_string = year + "-" + month + "-" + day + " " + endHour + ":" + endMinute + ":" + "00"
    activity = Activity(activity_id.get(), activity_name.get(), start_time_string, end_time_string,
                        activity_location.get())
    db_controller.add_activity(activity, logged_admin_id)
    db_controller.add_activity_to_admin(activity_id.get(), logged_admin_id)
    members_id = db_controller.added_members(logged_admin_id)
    for i in members_id:
        db_controller.add_activity_to_member(logged_admin_id, activity_id.get(), i, " ")
    refreshActivity(logged_admin_id)




def addAttendingMember():
    # need to have curse selection for multiple
    print("add attending member to the activity")


def admin_login():
    print("admin login session started")
    # implement whatever needed to check for login
    logged_admin_curse = db_controller.retrieve_admin(login_account.get())
    if not db_controller.admin_login(login_account.get(), login_password.get()):
        print('error')
        screenMember = Toplevel(screen)
        screenMember.title("Error")
        screen_width = screen.winfo_screenwidth() / 4
        screen_height = screen.winfo_screenheight() / 4
        xCoor = screen_width / 2 + 20
        yCoor = screen_height / 2 + 20

        screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))
    else:
        global screenAdmin
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        xCoor = screen_width / 2
        yCoor = screen_height / 2
        screenAdmin = Frame(screen, width=screen_width, height=screen_height)
        screenAdmin.grid(row=0, column=0)
        screen.title("Administrator %s" % logged_admin_curse["name"])

        leftFrame = Frame(screenAdmin, padx=10, pady=10)
        leftFrame.place(x=0, y=2, width=screen_width / 2, height=screen_height / 3)
        Button(leftFrame, text="Member Management", font=("new roman", 20), height=2, width=25,
               command=lambda: memberManagement(login_account.get())).grid(row=0, column=0)
        Label(leftFrame, text="", height=1, width=25).grid(row=1, column=0)
        Button(leftFrame, text="Activity Management", font=("new roman", 20), height=2, width=25,
               command=lambda: activityManagement(login_account.get())).grid(row=2, column=0)

        Button(screenAdmin, text="Log out", font=("new roman", 13), command=lambda: raise_frame(login_page)).place(
            x=screen_width - 70, y=screen_height - 25)

        memberManagement(logged_admin_curse["_id"])


def showPendingMember(logged_admin_id):
    global pendingMemberBox
    pendingMemberBox.delete(0, tk.END)
    for i in db_controller.pending_members(logged_admin_id):
        member_curse = db_controller.retrieve_member(i)
        pendingMemberBox.insert(END, "ID: " + member_curse["_id"] + "  " + "Name: " + member_curse["name"])


def showCurrentMember(logged_admin_id):
    global currentMemberBox
    currentMemberBox.delete(0, tk.END)
    for i in db_controller.added_members(logged_admin_id):
        member_curse = db_controller.retrieve_member(i)
        currentMemberBox.insert(END, "ID: " + member_curse["_id"] + "  " + "Name: " + member_curse["name"])


def rejectMember(logged_admin_id):
    if pendingMemberBox.curselection() != ():
        clicked_item_index = pendingMemberBox.curselection()[0]
        rej_member_id = db_controller.pending_members(logged_admin_id)[clicked_item_index]
        rej_member_email = db_controller.retrieve_member(rej_member_id)["email_address"]
        admin_name = db_controller.retrieve_admin(logged_admin_id)["name"]
        pendingMemberBox.delete(clicked_item_index)
        db_controller.remove_member_from_pending_members(logged_admin_id, rej_member_id)
        refreshList(logged_admin_id)
        db_controller.reject(rej_member_email, logged_admin_id, admin_name)


def acceptMember(logged_admin_id):
    if pendingMemberBox.curselection() != ():
        clicked_item_index = pendingMemberBox.curselection()[0]
        acc_member_id = db_controller.pending_members(logged_admin_id)[clicked_item_index]
        acc_member_email = db_controller.retrieve_member(acc_member_id)["email_address"]
        admin_name = db_controller.retrieve_admin(logged_admin_id)["name"]
        pendingMemberBox.delete(clicked_item_index)
        db_controller.add_member_to_added_members(logged_admin_id, acc_member_id)
        db_controller.remove_member_from_pending_members(logged_admin_id, acc_member_id)
        for i in db_controller.admin_activities(logged_admin_id):
            db_controller.add_activity_to_member(logged_admin_id, i, acc_member_id, " ")
        db_controller.add_club_to_member(logged_admin_id, acc_member_id)
        refreshList(logged_admin_id)
        refreshMember(logged_admin_id)
        db_controller.permit(acc_member_email, logged_admin_id, admin_name)


def deleteMember(logged_admin_id):
    if currentMemberBox.curselection() != ():
        clicked_item_index = currentMemberBox.curselection()[0]
        del_member_id = db_controller.added_members(logged_admin_id)[clicked_item_index]
        db_controller.remove_member_from_added_members(logged_admin_id, del_member_id)
        db_controller.remove_club_from_member(logged_admin_id, del_member_id)
        for i in db_controller.admin_activities(logged_admin_id):
            db_controller.remove_activity_from_member(logged_admin_id, i, del_member_id)
        currentMemberBox.delete(clicked_item_index)


def refreshMember(logged_admin_id):
    showCurrentMember(logged_admin_id)


def refreshList(logged_admin_id):
    showPendingMember(logged_admin_id)


def viewMember(logged_admin_id):
    if currentMemberBox.curselection() != ():
        clicked_item_index = currentMemberBox.curselection()[0]

        view_member_id = db_controller.added_members(logged_admin_id)[clicked_item_index]

        member_curse = db_controller.retrieve_member(view_member_id)

        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        bottomFrame = LabelFrame(screenAdmin, padx=10, pady=5)
        bottomFrame.place(x=5, y=screen_height / 3 + 2, width=screen_width / 2 - 5,
                          height=int(screen_height * 2 / 3 - 10))
        Label(bottomFrame, text="Member Status", font=("new roman", 15)).pack()

        infoFrame = Frame(bottomFrame, padx=1, pady=3)
        Label(infoFrame, text="Name: ", font=("new roman", 13)).grid(row=0, column=0, sticky=W)
        Label(infoFrame, text=member_curse["name"], font=("new roman", 13)).grid(row=0, column=1, sticky=W)
        Label(infoFrame, text="ID: ", font=("new roman", 13)).grid(row=1, column=0, sticky=W)
        Label(infoFrame, text=member_curse["_id"], font=("new roman", 13)).grid(row=1, column=1, sticky=W)
        Label(infoFrame, text="Email: ", font=("new roman", 13)).grid(row=2, column=0, sticky=W)
        Label(infoFrame, text=member_curse["email_address"], font=("new roman", 13)).grid(row=2, column=1, sticky=W)
        Label(infoFrame, text="Attendance Rate:    ", font=("new roman", 13)).grid(row=3, column=0, sticky=W)
        Label(infoFrame, text="50", font=("new roman", 13)).grid(row=3, column=1, sticky=W)
        infoFrame.pack()

        global joinedActivityBox
        global joinedFrame
        global joinedScroll
        joinedFrame = Frame(bottomFrame, padx=3, pady=5, height=int(screen_height / 6))
        Label(joinedFrame, text="Past Activities", font=("new roman", 13)).pack()
        joinedScroll = Scrollbar(joinedFrame)
        joinedScroll.pack(side=RIGHT, fill=Y)
        joinedActivityBox = Listbox(joinedFrame, yscrollcommand=joinedScroll.set, width=int(screen_width / 2 - 7),
                                    height=4,
                                    selectmode=SINGLE)

        show_member_status(logged_admin_id, view_member_id)

        joinedActivityBox.pack(side=LEFT)
        joinedScroll.config(command=joinedActivityBox.yview)
        joinedFrame.pack()


def show_member_status(logged_admin_id, view_member_id):
    global joinedActivityBox
    for j in db_controller.admin_activities(logged_admin_id):
        activity_curse = db_controller.retrieve_activity(j)
        status = db_controller.member_status_in_activity(view_member_id, logged_admin_id, j)
        joinedActivityBox.insert(END, "Activity_ID:  " + str(activity_curse["_id"])+ "  " + "Activity_name:  " + activity_curse["name"] + "  " + "Status:  " + status)
        '''+ "Activity_name:  " + activity_curse["name"] + "  "
                                        + "Status:  " + status)'''


def member():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="User ID                            ", font=("new roman", 21)).place(x=screen_width / 24,
                                                                                            y=screen_height * 2 / 30)
    Button(screen, text="New Member Register", font=("new roman", 15), height="5", width="20", command=member_register,
           fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Member Login", font=("new roman", 15), height="5", width="20", command=member_login,
           fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)


def display_password():
    if (show_password.get()):
        login_password_entry.config(show="")
    else:
        login_password_entry.config(show="*")


def login():
    print("Login session started")


def forget():
    print("to be developed")


main_screen()
