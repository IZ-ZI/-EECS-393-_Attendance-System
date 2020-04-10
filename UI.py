from tkinter import *
from Administrator import Administrator
from Member import Member

screen = None

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

screenAdmin = None

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

administrator_list = []
member_list = []
current_member_list = []
pending_member_list = []
added_club_list=[]

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


def main_screen():
    global screen

    global administrator_list
    administrator_list = []
    global member_list
    member_list = []

    screen = Tk()
    screen.geometry("600x300")
    screen.title("Attendance System Login")
    # screen.configure(background='turquoise')

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    xCoor = screen_width / 2
    yCoor = screen_height / 2

    screen.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))

    global login_account_entry
    global login_password_entry
    global login_account
    global login_password
    global show_password

    login_account = StringVar()
    login_password = StringVar()

    Label(screen, text="Club/Organization ID", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height / 30)

    # member_email_entry = Entry(screen1, textvariable=member_email)

    login_account_entry = Entry(screen, textvariable=login_account, width="20")
    login_account_entry.place(x=screen_width / 30, y=screen_height * 3 / 30)

    Label(screen, text="Password", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height * 10 / 30)
    show_password = BooleanVar()
    Checkbutton(screen, text="show password", variable=show_password, command=display_password).place(x=screen_width / 35, y=screen_height * 15 / 30)
    login_password_entry = Entry(screen, show='*', textvariable=login_password, width="20")
    login_password_entry.place(x=screen_width / 30, y=screen_height * 13 / 30)

    # highlightbackground = 'green'

    Button(screen, text="Administrator", height="5", width="20", command=admin, fg='black').place(
        x=screen_width * 2 / 3, y=screen_height / 30)
    Button(screen, text="Member", height="5", width="20", command=member, fg='black', ).place(x=screen_width * 2 / 3,
                                                                                              y=screen_height / 4 + screen_height / 30)

    Button(screen, text="Administrator Login", height="5", width="20", command=admin_login, fg='black').place(
        x=screen_width / 30,
        y=screen_height * 2 / 3)
    # Button(screen, text="Login", height= "3", width = "20", command = login, fg='black').grid(row=6, column=0)
    Button(screen, text="Forget/Reset Password", height="5", width="20", command=forget, fg='black').place(
        x=screen_width / 3 + screen_width / 30, y=screen_height * 2 / 3)

    Button(screen, text="New Club Register", height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)

    # global button
    # button = Button(screen,text='Submit',command=changeText)
    # button.pack()

    screen.mainloop()


def club_register_check():
    global club_password  # do this

    if (club_password.get() != club_confirm_password.get()):
        club_register_feedback['text'] = 'Password difference'
        # club_register_feedback.set("Password Difference")
    elif (
            club_id.get() == '' or club_name.get() == '' or club_email.get() == '' or club_password.get() == '' or club_confirm_password.get() == ''):
        club_register_feedback['text'] = 'Please fill all the spaces'
    elif (
            id_to_admin(club_id.get()) is not None):
        club_register_feedback['text'] = 'This id has already been registered'
    else:
        club_info()


def member_register_check():
    if (member_password.get() != member_confirm_password.get()):
        member_register_feedback['text'] = 'Password difference'
    elif (
            member_id.get() == '' or member_name.get() == '' or member_email.get() == '' or member_password.get() == '' or member_confirm_password.get() == '' or member_apply_club_id.get() == ''):
        member_register_feedback['text'] = 'Please fill all the spaces'
    elif (
            id_to_member(member_id.get()) is not None):
        member_register_feedback['text'] = 'User id has already been registered'
    elif (
            id_to_admin(member_apply_club_id.get()) is None):
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
    global administrator_list

    administrator = Administrator(club_name.get(), club_id.get(), club_email.get(), club_password.get())
    administrator_list.append(administrator)

    club_id_entry.delete(0, END)
    club_name_entry.delete(0, END)
    club_email_entry.delete(0, END)
    club_password_entry.delete(0, END)
    club_confirm_password_entry.delete(0, END)

    club_register_feedback['text'] = 'Registration Success'


def id_to_admin(id):
    global administrator_list
    for i in administrator_list:
        if i.get_organization_id() == id:
            return i
    return None


def id_to_member(id):
    global member_list
    for i in member_list:
        if i.get_id() == id:
            return i
    return None


def id_to_member(id):
    global member_list
    for i in member_list:
        if i.get_id() == id:
            return i
    return None


def member_info():
    # file = open(member_id.get() + ".txt", "w")
    # file.write(member_id.get() + "\n")
    # file.write(member_name.get() + "\n")
    # file.write(member_email.get() + "\n")
    # file.write(member_password.get() + "\n")
    # file.write(member_confirm_password.get() + "\n")
    # file.write(member_apply_club_id.get() + "\n")
    # file.close()
    global member_list
    new_member = Member(member_name.get(), member_id.get(), member_email.get(), member_password.get())
    member_list.append(new_member)

    administrator = id_to_admin(member_apply_club_id.get())

    administrator.pend_member(new_member)
    member_register_feedback['text'] = 'Registration Success'
    new_member.requestPermission(administrator)

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
    Label(screen, text="Club/Organization ID", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height * 2/ 30)
    Button(screen, text="New Club Register", font = ("new roman", 15),height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Administrator Login", font = ("new roman", 15),height= "5", width = "20", command = admin_login, fg='black').place(
        x = screen_width/30, y = screen_height*2/3)


def member_login():
    global screenMember
    print("member login session started")
    print('%s' % login_account_entry)
    # implement whatever needed to check for login
    logged_member = id_to_member(login_account.get())
    if logged_member is None or logged_member.get_password() != login_password.get():
        print('error')
        screenMember = Toplevel(screen)
        screenMember.title("Error")
        screen_width = screen.winfo_screenwidth() / 4
        screen_height = screen.winfo_screenheight() / 4
        xCoor = screen_width / 2 + 20
        yCoor = screen_height / 2 + 20

        screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))
    else:
        screenMember = Toplevel(screen)
        screenMember.title("Member: %s" % logged_member.get_name())
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        xCoor = screen_width / 2 + 20
        yCoor = screen_height / 2 + 20
        screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))

        frame = Frame(screenMember, padx=10, pady=10)
        frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height)

        global clubBox
        global clubScroll
        global clubFrame
        Label(frame, text="Clubs", font=("new roman", 21)).pack()
        clubFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
        clubScroll = Scrollbar(clubFrame)
        clubScroll.pack(side=RIGHT, fill=Y)
        clubBox = Listbox(clubFrame, yscrollcommand=clubScroll.set, width=int(screen_width / 8), height=20,
                          selectmode=SINGLE)

        show_club_list(logged_member)

        clubBox.pack(side=LEFT)
        clubScroll.config(command=clubBox.yview)
        clubFrame.pack()
        Button(frame, text="Refresh", font=("new roman", 18), height=1, width=10,
               command=lambda: refreshClub(logged_member)).pack()

def show_club_list(logged_member):
    global clubBox
    global added_club_list
    for i in logged_member.admin_list:
        if (i not in added_club_list):
            added_club_list.append(i)
            clubBox.insert(END,  "ID: " + i.get_organization_id() + "  " + "Name: " + i.get_organization_name())


def refreshClub(logged_member):
    show_club_list(logged_member)


def memberManagement():
    frame = Frame(screenAdmin, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height)

    Label(frame, text="Current Members", font=("new roman", 21)).pack()

    global currentMemberBox
    global currentScroll
    global currentFrame
    currentFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
    currentScroll = Scrollbar(currentFrame)
    currentScroll.pack(side=RIGHT, fill=Y)
    currentMemberBox = Listbox(currentFrame, yscrollcommand=currentScroll.set, width=int(screen_width / 8),
                                   height=7, selectmode=SINGLE)
    showCurrentMember(logged_admin)

    currentMemberBox.pack(side=LEFT)
    currentScroll.config(command=currentMemberBox.yview)
    currentFrame.pack()

    buttonFrameC = Frame(frame, padx=1, pady=3)
    Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=9,
               command=lambda: refreshMember(logged_admin)).grid(
            row=0, column=0)

    Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=9,
               command=lambda: viewMember(logged_admin)).grid(row=0, column=1)

    Button(buttonFrameC, text="Delete", font=("new roman", 18), height=1, width=9, command=deleteMember).grid(
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
               command=lambda: refreshList(logged_admin)).grid(row=0,
                                                                      column=0)
    Button(buttonFrameP, text="Accept", font=("new roman", 18), height=1, width=9, command=lambda:acceptMember(logged_admin)).grid(row=0,
                                                                                                                  column=1)
    Button(buttonFrameP, text="Reject", font=("new roman", 18), height=1, width=9, command=lambda:rejectMember(logged_admin)).grid(row=0,
                                                                                                                  column=2)
    buttonFrameP.pack()

    showPendingMember(logged_admin)


def activityManagement():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenAdmin, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height)
    Label(frame, text = "Activities", font = ("new roman", 21)).pack()

    global activityBox
    activityFrame = Frame(frame, padx = 1, pady = 3, height = int(screen_height / 2))
    activityScroll = Scrollbar(activityFrame)
    activityScroll.pack(side = RIGHT, fill = Y)
    activityBox = Listbox(activityFrame, yscrollcommand = activityScroll.set, width = int(screen_width/8), height = 19, selectmode = SINGLE)

    for i in range(1, 20):
        activityBox.insert(END, "LINE " + str(i))

    activityBox.pack(side = LEFT)
    activityScroll.config(command = currentMemberBox.yview)
    activityFrame.pack()

    buttonFrameA = Frame(frame, padx = 1, pady=3)
    Button(buttonFrameA, text = "Refresh", font = ("new roman", 18), height = 1, width = 9, command = refreshActivity).grid(row = 0, column = 0)
    Button(buttonFrameA, text = "View", font = ("new roman", 18), height = 1, width = 9, command = viewActivity).grid(row = 0, column = 1)
    Button(buttonFrameA, text = "Create", font = ("new roman", 18), height = 1, width = 9, command = createActivity).grid(row = 0, column = 2)
    buttonFrameA.pack()

    bottomFrame = Frame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))

def refreshActivity():
    print("refresh activity")


def updateTime():
    print("update time")

def refreshActivityInfo():
    print("refresh activity info, including member list and time")

def viewActivity():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    bottomFrame = LabelFrame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))
    Label(bottomFrame, text = "Activity Status", font = ("new roman", 15)).pack()

    timeFrame = Frame(bottomFrame, padx = 1, pady = 3)
    Label(timeFrame, text = "Start Time", font = ("new roman", 13)).grid(row = 0, column = 0)
    Label(timeFrame, text = "         ").grid(row = 0, column = 1)
    Label(timeFrame, text = "End Time", font = ("new roman", 13)).grid(row = 0, column = 2)
    #pull out information about the start time and end time
    Label(timeFrame, text = "12:00", font = ("new roman", 13)).grid(row = 1, column = 0)
    Label(timeFrame, text = "         ").grid(row = 1, column = 1)
    Label(timeFrame, text = "14:00", font = ("new roman", 13)).grid (row = 1, column = 2)
    timeFrame.pack()

    buttonFrame = Frame(bottomFrame, padx = 1, pady = 2)
    Button(buttonFrame, text = "Update Time", font = ("new roman", 13), width = 16, height = 2, command = updateTime).grid(row = 0, column = 0)
    Button(buttonFrame, text = "Refresh Information", font = ("new roman", 13), width = 16, height = 2, command = refreshActivityInfo).grid(row = 0, column = 1)
    buttonFrame.pack()

    global attendingMemberBox
    attendingFrame = Frame(bottomFrame, padx = 3, pady = 4, height = int(screen_height/6))
    Label(attendingFrame, text = "Attending Members", font = ("new roman", 13)).pack()
    attendingScroll = Scrollbar(attendingFrame)
    attendingScroll.pack(side = RIGHT, fill = Y)
    attendingMemberBox = Listbox(attendingFrame, yscrollcommand = attendingScroll.set, width = int(screen_width/2 - 7), height = 4, selectmode = SINGLE)

    for i in range(1, 15):
        attendingMemberBox.insert(END, "LINE" + str(i))

    attendingMemberBox.pack(side = LEFT)
    attendingScroll.config(command = attendingMemberBox.yview)
    attendingFrame.pack()

    attendanceFrame = Frame(bottomFrame, padx = 2, pady = 3)
    Button(attendanceFrame, text = "Take Attendance", font = ("new roman", 13), width = 16, height = 2, command = takeAttendance).grid(row = 0, column = 0)
    Button(attendanceFrame, text = "Generate Report", font = ("new roman", 13), width = 16, height = 2, command = generateActivityReport).grid(row = 0, column = 1)
    attendanceFrame.pack()

def takeAttendance():
    print("taking attendance")
    global screenAttendance
    screenAttendance = Toplevel(screenAdmin)
    screenAttendance.title("Taking Attendance")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    screenAttendance.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))


    leftFrame = Frame(screenAttendance, padx=10, pady=10)
    leftFrame.place(x=0, y=2, width=screen_width / 2, height=int(screen_height*2/3))
    Label(leftFrame, text = "Member ID", font = ("new roman", 15)).grid(row = 0, column = 0, sticky = W)
    memberid_entry = Entry(leftFrame, width = 20)
    memberid_entry.grid(row = 1, column = 0)
    Button(leftFrame, text = "OK", font = ("new roman", 15), command = getMemberPhoto).grid(row = 1, column = 1)
    Label(leftFrame, text = "").grid(row = 2, column = 0)
    Label(leftFrame, text = "Photo on File", font = ("new roman", 15)).grid(row = 3, column = 0, sticky = W)
    photoFrame = LabelFrame(leftFrame, padx = 10, pady = 10, width = screen_width/4, height = screen_width/4)
    photoFrame.grid(row = 4, column = 0)


    rightFrame = Frame(screenAttendance, padx = 10, pady = 10)
    rightFrame.place(x = screen_width / 2, y = 2, width = screen_width/2, height = int(screen_height*2/3))
    Label(rightFrame, text = "Camera", font = ("new roman", 15)).grid(row = 0, column = 0, sticky = W)

def getMemberPhoto():
    print("get Member Photo")

def generateActivityReport():
    print("generating report")

def createActivity():
    print("create activity")
    global screenCreateActivity
    screenCreateActivity = Toplevel(screenAdmin)
    screenCreateActivity.title("New Activity")
    screenCreateActivity.geometry("400x600+10+10")
    # 1
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Activity Name").pack()
    activity_entry = Entry(screenCreateActivity)
    activity_entry.pack()
    # 2
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Date").pack()
    date_entry = Entry(screenCreateActivity)
    date_entry.pack()
    # 3
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Start Time").pack()
    starttime_entry = Entry(screenCreateActivity)
    starttime_entry.pack()
    # 4
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "End Time").pack()
    endtime_entry = Entry(screenCreateActivity)
    endtime_entry.pack()

    global memberBox
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Select attending members below").pack()
    currentFrame = Frame(screenCreateActivity, padx = 10, pady = 3, width = 400)
    currentScroll = Scrollbar(currentFrame)
    currentScroll.pack(side = RIGHT, fill = Y)
    memberBox = Listbox(currentFrame, yscrollcommand = currentScroll.set, width = 400, height = 7, selectmode = MULTIPLE)

    for i in range(1, 15):
        memberBox.insert(END, "LINE " + str(i))

    memberBox.pack(side = LEFT)
    currentScroll.config(command = memberBox.yview)
    currentFrame.pack()

    Button(screenCreateActivity, text = "Add Attending Members", height = 2, width = 20, command = addAttendingMember).pack()

    Label(screenCreateActivity, text = "").pack()
    Button(screenCreateActivity, text="Create Activity", height= 3, width = 20, command = newActivity).pack()

def newActivity():
    print("create new activity")

def addAttendingMember():
    #need to have curse selection for multiple
    print("add attending member to the activity")

def admin_login():
    print("admin login session started")
    # implement whatever needed to check for login
    logged_admin = id_to_admin(login_account.get())
    if logged_admin is None or logged_admin.get_password() != login_password.get():
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
        screenAdmin = Toplevel(screen)
        screenAdmin.title("Administrator %s" % logged_admin.get_organization_name())
        screen_width = screen.winfo_screenwidth() / 2
        screen_height = screen.winfo_screenheight() / 2
        xCoor = screen_width / 2
        yCoor = screen_height / 2
        screenAdmin.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))


        leftFrame = Frame(screenAdmin, padx = 10, pady = 10)
        leftFrame.place(x = 0, y = 2, width = screen_width/2, height = screen_height/3)
        Button(leftFrame, text = "Member Management", font = ("new roman", 20), height = 2, width = 25, command = memberManagement).grid(row = 0, column = 0)
        Label(leftFrame, text = "", height = 1, width = 25).grid(row = 1, column = 0)
        Button(leftFrame, text = "Activity Management", font = ("new roman", 20), height = 2, width = 25, command = activityManagement).grid(row = 2, column = 0)
        
        frame = Frame(screenAdmin, padx=10, pady=10)
        frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height)

        Label(frame, text="Current Members", font=("new roman", 21)).pack()

        global currentMemberBox
        global currentScroll
        global currentFrame
        currentFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
        currentScroll = Scrollbar(currentFrame)
        currentScroll.pack(side=RIGHT, fill=Y)
        currentMemberBox = Listbox(currentFrame, yscrollcommand=currentScroll.set, width=int(screen_width / 8),
                                   height=7, selectmode=SINGLE)

        showCurrentMember(logged_admin)

        currentMemberBox.pack(side=LEFT)
        currentScroll.config(command=currentMemberBox.yview)
        currentFrame.pack()

        buttonFrameC = Frame(frame, padx=1, pady=3)
        Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=9,
               command=lambda: refreshMember(logged_admin)).grid(
            row=0, column=0)

        Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=9,
               command=lambda: viewMember(logged_admin)).grid(row=0, column=1)

        Button(buttonFrameC, text="Delete", font=("new roman", 18), height=1, width=9, command=deleteMember).grid(
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
               command=lambda: refreshList(logged_admin)).grid(row=0,
                                                                      column=0)
        Button(buttonFrameP, text="Accept", font=("new roman", 18), height=1, width=9, command=lambda:acceptMember(logged_admin)).grid(row=0,
                                                                                                                  column=1)
        Button(buttonFrameP, text="Reject", font=("new roman", 18), height=1, width=9, command=lambda:rejectMember(logged_admin)).grid(row=0,
                                                                                                                  column=2)
        buttonFrameP.pack()

        showPendingMember(logged_admin)


def showPendingMember(logged_admin):
    global pendingMemberBox
    global pending_member_list
    for i in logged_admin.get_member_database().wait_list:
        if(i not in pending_member_list):
            pending_member_list.append(i)
            pendingMemberBox.insert(END,  "ID: " + i.get_id() + "  " + "Name: " + i.get_name())



def showCurrentMember(logged_admin):
    # loop for Current Member List
    # while member in MemberList:
    global currentMemberBox
    global current_member_list
    for i in logged_admin.get_member_database().database:
        if(i not in current_member_list):
            current_member_list.append(i)
            currentMemberBox.insert(END,  "ID: " + i.get_id() + "  " + "Name: " + i.get_name())



def rejectMember(logged_admin):
    global pending_member_list
    if pendingMemberBox.curselection() != ():
        clicked_item_index = pendingMemberBox.curselection()[0]
        rej_member = logged_admin.get_member_database().wait_list[clicked_item_index]
        logged_admin.get_member_database().reject_pending_member(rej_member.get_id())
        pendingMemberBox.delete(clicked_item_index)
        refreshList(logged_admin)
        logged_admin.reject(rej_member)


def acceptMember(logged_admin):
    if pendingMemberBox.curselection() != ():
        clicked_item_index = pendingMemberBox.curselection()[0]
        acc_member = logged_admin.get_member_database().wait_list[clicked_item_index]
        acc_member.admin_list.append(logged_admin)
        logged_admin.get_member_database().permit_pending_member(acc_member.get_id())
        pendingMemberBox.delete(clicked_item_index)
        refreshList(logged_admin)
        refreshMember(logged_admin)
        logged_admin.permit(acc_member)


def deleteMember():
    clicked_items = currentMemberBox.curselection()
    currentMemberBox.delete(clicked_items)


def refreshMember(logged_admin):
    showCurrentMember(logged_admin)


def refreshList(logged_admin):
    showPendingMember(logged_admin)


def viewMember(logged_admin):
    if currentMemberBox.curselection() != ():
        clicked_item_index = currentMemberBox.curselection()[0]

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    bottomFrame = LabelFrame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))
    Label(bottomFrame, text = "Member Status", font = ("new roman", 15)).pack()

    infoFrame = Frame(bottomFrame, padx = 1, pady = 3)
    Label(infoFrame, text = "Name: ", font = ("new roman", 13)).grid(row = 0, column = 0)
    Label(infoFrame, text = "Han Pi", font = ("new roman", 13)).grid(row = 0, column = 1)
    Label(infoFrame, text = "ID: ", font = ("new roman", 13)).grid(row = 1, column = 0)
    Label(infoFrame, text = "hxp342", font = ("new roman", 13)).grid(row = 1, column = 1)
    Label(infoFrame, text = "Email: ", font = ("new roman", 13)).grid(row = 2, column = 0)
    Label(infoFrame, text = "hxp342@case.edu", font = ("new roman", 13)).grid (row = 2, column = 1)
    infoFrame.pack()

    global joinedActivityBox
    joinedFrame = Frame(bottomFrame, padx = 3, pady = 5, height = int(screen_height/6))
    Label(joinedFrame, text = "Past Activities", font = ("new roman", 13)).pack()
    joinedScroll = Scrollbar(joinedFrame)
    joinedScroll.pack(side = RIGHT, fill = Y)
    joinedActivityBox = Listbox(joinedFrame, yscrollcommand = joinedScroll.set, width = int(screen_width/2 - 7), height = 4, selectmode = SINGLE)

    for i in range(1, 15):
        joinedActivityBox.insert(END, "LINE" + str(i))

    joinedActivityBox.pack(side = LEFT)
    joinedScroll.config(command = joinedActivityBox.yview)
    joinedFrame.pack()

    Button(bottomFrame, text = "Generate Attendance Report", font = ("new roman", 13), width = 20, height = 2, command = generateMemberReport).pack()

def generateMemberReport():
    print("generate member report")


def member():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="User ID                            ", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height * 2/ 30)
    Button(screen, text="New Member Register", font = ("new roman", 15),height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Member Login", font = ("new roman", 15),height="5", width="20", command=member_login, fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)


def display_password():
    if(show_password.get()):
        login_password_entry.config(show="")
    else:
        login_password_entry.config(show="*")

def login():
    print("Login session started")


def forget():
    print("to be developed")


main_screen()
