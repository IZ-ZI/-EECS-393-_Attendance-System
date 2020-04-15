from tkinter import *

def main_screen():
    global screen
    screen = Tk()
    screen.title("Attendance System Login")

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    xCoor = screen_width /2
    yCoor = screen_height / 2

    screen.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor,yCoor))

    global login_page
    login_page = Frame(screen, width = screen_width, height = screen_height)
    login_page.grid(row = 0, column = 0)

    Label(login_page, text="Club/Organization ID", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height*2 / 30)
    Entry(login_page,width = "30").place(x=screen_width / 24, y=screen_height * 5/30)
    Label(login_page, text="Password",font=("new roman", 21)).place(x=screen_width/24, y=screen_height*10/30)
    Entry(login_page,width = "30").place(x = screen_width / 24, y= screen_height*13/30)

    # highlightbackground = 'green'

    Button(login_page, text="Administrator", font = ("new roman", 15), height="5", width="20", command = admin, fg='black', ).place(x=screen_width*6.5/10, y=screen_height/25)
    Button(login_page, text="Member", font = ("new roman", 15),height= "5", width ="20", command = member, fg='black', ).place(x = screen_width *6.5/10, y = screen_height/4+screen_height/30)

    Button(login_page, text="Administrator Login",font = ("new roman", 15), height= "5", width = "20", command = admin_login, fg='black').place(x = screen_width/30, y = screen_height*2/3)
   # Button(screen, text="Login", height= "3", width = "20", command = login, fg='black').grid(row=6, column=0)
    Button(login_page, text="Forget/Reset Password", font = ("new roman", 15),height= "5", width = "20", command = forget, fg='black').place(x=screen_width/3 + screen_width/30, y=screen_height*2/3)

    Button(login_page, text="New Club Register", font = ("new roman", 15),height= "5", width = "20", command = club_register, fg='black').place(x=screen_width*2/3+screen_width/30, y=screen_height*2/3)

    raise_frame(login_page)
    screen.mainloop()

def raise_frame(frame):
    frame.tkraise()
    screen.title("Attendance System Login")



def club_info():
    username_info = password.get()
    password_info = password.get()

    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(screen1, text = "Registration sent", fg = "green", font=("new roman", 15)).pack()

def club_register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("New Club Registration")
    screen1.geometry("600x570")

    global clubname
    global password
    global username_entry
    global password_entry
    clubname = StringVar()
    password = StringVar()


    # 1
    Label(screen1, text = "").pack()
    Label(screen1, text = "Club/Organization ID").pack()
    username_entry = Entry(screen1, textvariable = password)
    username_entry.pack()
    # 2
    Label(screen1, text = "").pack()
    Label(screen1, text = "Name of the Club/Organization").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    # 3
    Label(screen1, text = "").pack()
    Label(screen1, text = "Club/Organization Email").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    # 4
    Label(screen1, text = "").pack()
    Label(screen1, text = "Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    # 5
    Label(screen1, text = "").pack()
    Label(screen1, text = "Confirm Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    # 6
    Label(screen1, text = "").pack()
    Button(screen1, text="Register", height= "3", width = "20", command = club_info).pack()


def member_register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("New Club Registration")
    screen1.geometry("600x570")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    # 1
    Label(screen1, text="").pack()
    Label(screen1, text="Name").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    # 2
    Label(screen1, text="").pack()
    Label(screen1, text="User ID").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    # 3
    Label(screen1, text="").pack()
    Label(screen1, text="Email").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    # 4
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    # 6
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization ID").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    # 7
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="20", command= club_info).pack()


def admin():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="Club/Organization ID", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height * 2/ 30)
    Button(screen, text="New Club Register", font = ("new roman", 15),height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Administrator Login", font = ("new roman", 15),height= "5", width = "20", command = admin_login, fg='black').place(
        x = screen_width/30, y = screen_height*2/3)
def member():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="User ID                            ", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height * 2/ 30)
    #Label(screen, text = "", height = 2, width = 30).place(x=screen_width* 2.1 /15, y = screen_height *2/30)
    Button(screen, text="New Member Register", font = ("new roman", 15),height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Member Login", font = ("new roman", 15),height="5", width="20", command=member_login, fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)



def clubList():
    print("show my clubs")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    frame = Frame(screenMember, padx = 10, pady = 10)
    frame.place(x=screen_width/2, y=2, width = screen_width/2, height = screen_height - 27)

    global clubBox
    Label(frame, text = "Clubs", font = ("new roman", 21)).pack()
    clubFrame = Frame(frame, padx= 1, pady = 3, height = int(screen_height / 5))
    clubScroll = Scrollbar(clubFrame)
    clubScroll.pack(side = RIGHT, fill = Y)
    clubBox = Listbox(clubFrame, yscrollcommand = clubScroll.set, width = int(screen_width/8), height = 19, selectmode = SINGLE)

    for i in range(1, 20):
        clubBox.insert(END, "LINE " + str(i))

    clubBox.pack(side = LEFT)
    clubScroll.config(command = clubBox.yview)
    clubFrame.pack()


    buttonFrameC = Frame(frame, padx=1, pady=3)
    Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=7, command=refreshClubList).grid(row=0, column=0)
    Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=6, command=viewClub).grid(row=0, column=1)
    Button(buttonFrameC, text = "Apply", font = ("new roman", 18), height = 1, width = 7, command = applyClub).grid(row = 0, column = 2)
    Button(buttonFrameC, text="Leave", font=("new roman", 18), height=1, width=6, command=deleteClub).grid(row=0, column=3)
    buttonFrameC.pack()

    bottomFrame = Frame(screenMember, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))


def applyClub():
    global applyClubScreen
    applyClubScreen = Toplevel(screen)
    applyClubScreen.geometry("300x200+30+30")
    applyClubScreen.title("Apply for New Club")
    Label(applyClubScreen, text = "").pack()
    Label(applyClubScreen, text = "Club ID", font = ("new roman", 18)).pack()
    clubID_entry = Entry(applyClubScreen)
    clubID_entry.pack()
    Label(applyClubScreen,text = "").pack()
    Button(applyClubScreen, text = "Apply", width = 20, height = 2, command = submitClubID).pack()

def submitClubID():
    print("submit...")






def activityList():
    print("show my activities")

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    frame = Frame(screenMember, padx = 10, pady = 10)
    frame.place(x=screen_width/2, y=2, width = screen_width/2, height = screen_height - 27)

    global myActivityBox
    Label(frame, text = "Activities", font = ("new roman", 21)).pack()
    myActivityFrame = Frame(frame, padx= 1, pady = 3, height = int(screen_height / 5))
    myActivityScroll = Scrollbar(myActivityFrame)
    myActivityScroll.pack(side = RIGHT, fill = Y)
    myActivityBox = Listbox(myActivityFrame, yscrollcommand = myActivityScroll.set, width = int(screen_width/8), height = 19, selectmode = SINGLE)

    for i in range(1, 20):
        myActivityBox.insert(END, "LINE " + str(i))

    myActivityBox.pack(side = LEFT)
    myActivityScroll.config(command = myActivityBox.yview)
    myActivityFrame.pack()


    buttonFrame = Frame(frame, padx=2, pady=3)
    Button(buttonFrame, text="Refresh", font=("new roman", 18), height=1, width=13, command=refreshMyActivity).grid(row=0, column=0)
    Label(buttonFrame, text = " ").grid(row = 0, column = 1)
    Button(buttonFrame, text="View", font=("new roman", 18), height=1, width=13, command=viewActivityStatus).grid(row=0, column=2)
    buttonFrame.pack()

    bottomFrame = Frame(screenMember, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))

def refreshMyActivity():
    print("refresh my activity list")

def setFaceID():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    global screenSetfaceID
    screenSetfaceID = Toplevel(screen)
    screenSetfaceID.title("Set Face ID")
    screenSetfaceID.geometry("%dx%d" % (screen_height, screen_height))
    Label(screenSetfaceID, text = "").pack()
    photoFrame = LabelFrame(screenSetfaceID, padx= 10, pady = 10, width = int (screen_height*2/3), height = int (screen_height*2/3))
    photoFrame.pack()
    Label(screenSetfaceID, text="").pack()
    Button(screenSetfaceID, text = "Take Face ID Photo", height = 3, width = 20, command = setIDSuccess).pack()


def takeFaceIDPhoto():
    #conditional statement needed
    print("take face id photo")

def setIDSuccess():
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenSetfaceID)
    Label(frame, text = "Success", fg = 'green').pack()
    frame.place(x = 0, y = screen_height - 50, width = screen_height)

def setIDFail():
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenSetfaceID)
    Label(frame, text = "Failed", fg = 'red').pack()
    Label(frame, text = "Please Try Again.", fg = 'red').pack()
    frame.place(x = 0, y = screen_height - 50, width = screen_height)




def member_login():
    print("member login session started")
    #implement whatever needed to check for login
    global screenMember

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    screenMember = Frame(screen, width = screen_width, height = screen_height)
    screenMember.grid(row = 0, column = 0)
    screen.title("Member")

    xCoor = screen_width /2+20
    yCoor = screen_height / 2+20
    #screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor,yCoor))

    Button(screenMember, text = "Log out", font = ("new roman", 13), command = lambda:raise_frame(login_page)).place(x = screen_width - 70, y = screen_height - 25)

    Button(screenMember, text = "Set Face ID", font = ("new roman", 13), width = 10, command = setFaceID).place(x = screen_width/2+10, y = screen_height - 25)

    leftFrame = Frame(screenMember, padx = 10, pady = 10)
    leftFrame.place(x = 0, y = 2, width = screen_width/2, height = screen_height/3)
    Button(leftFrame, text = "My Clubs", font = ("new roman", 20), height = 2, width = 25, command = clubList).grid(row = 0, column = 0)
    Label(leftFrame, text = "", height = 1, width = 25).grid(row = 1, column = 0)
    Button(leftFrame, text = "My Activities", font = ("new roman", 20), height = 2, width = 25, command = activityList).grid(row = 2, column = 0)

    frame = Frame(screenMember, padx = 10, pady = 10)
    frame.place(x=screen_width/2, y=2, width = screen_width/2, height = screen_height - 27)

    global clubBox
    Label(frame, text = "Clubs", font = ("new roman", 21)).pack()
    clubFrame = Frame(frame, padx= 1, pady = 3, height = int(screen_height / 5))
    clubScroll = Scrollbar(clubFrame)
    clubScroll.pack(side = RIGHT, fill = Y)
    clubBox = Listbox(clubFrame, yscrollcommand = clubScroll.set, width = int(screen_width/8), height = 19, selectmode = SINGLE)

    for i in range(1, 20):
        clubBox.insert(END, "LINE " + str(i))

    clubBox.pack(side = LEFT)
    clubScroll.config(command = clubBox.yview)
    clubFrame.pack()


    buttonFrameC = Frame(frame, padx=1, pady=3)
    Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=9, command=refreshClubList).grid(row=0,
                                                                                                            column=0)
    Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=9, command=viewClub).grid(row=0,
                                                                                                      column=1)
    Button(buttonFrameC, text="Leave", font=("new roman", 18), height=1, width=9, command=deleteClub).grid(row=0,
                                                                                                          column=2)
    buttonFrameC.pack()



def refreshClubList():
    print("refresh my clubs")


def viewClub():
    print("view club info and my status")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    bottomFrame = LabelFrame(screenMember, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))
    Label(bottomFrame, text = "Club Status", font = ("new roman", 15)).pack()

    clubInfoFrame = Frame(bottomFrame, padx = 1, pady = 1)
    Label(clubInfoFrame, text = "Club Name:", font = ("new roman", 13)).grid(row = 0, column = 0, sticky = W)
    Label(clubInfoFrame, text = "EECS 391").grid(row = 0, column = 1, sticky = W)
    Label(clubInfoFrame, text = "Club ID: ", font = ("new roman", 13)).grid(row = 1, column = 0, sticky = W)
    Label(clubInfoFrame, text = "123123", font = ("new roman", 13)).grid(row = 1, column = 1, sticky = W)
    Label(clubInfoFrame, text = "Total Number of Events:     ").grid(row = 2, column = 0, sticky = W)
    Label(clubInfoFrame, text = "15", font = ("new roman", 13)).grid (row = 2, column = 1, sticky = W)
    Label(clubInfoFrame, text = "My Absenses", font = ("new roman", 13)).grid(row = 3, column = 0, sticky = W)
    Label(clubInfoFrame, text = "3", font = ("new roman", 13)).grid(row = 3, column = 1, sticky = W)
    Label(clubInfoFrame, text = "Attendance Rate", font = ("new roman", 13)).grid(row = 4, column = 0, sticky = W)
    Label(clubInfoFrame, text = "80", font = ("new roman", 13)).grid(row = 4, column = 1, sticky = W)
    clubInfoFrame.pack()

    global clubActivityBox
    clubActivityFrame = Frame(bottomFrame, padx = 3, pady = 0, height = int(screen_height/6))
    Label(clubActivityFrame, text = "My Club Events", font = ("new roman", 13)).pack()
    clubActivityScroll = Scrollbar(clubActivityFrame)
    clubActivityScroll.pack(side = RIGHT, fill = Y)
    clubActivityBox = Listbox(clubActivityFrame, yscrollcommand = clubActivityScroll.set, width = int(screen_width/2 - 7), height = 4, selectmode = SINGLE)

    for i in range(1, 15):
        clubActivityBox.insert(END, "LINE" + str(i))

    clubActivityBox.pack(side = LEFT)
    clubActivityScroll.config(command = clubActivityBox.yview)
    clubActivityFrame.pack()

    Button(bottomFrame, text = "View Activity Status", font = ("new roman", 12), command = viewActivityStatus).pack()



def viewActivityStatus():
    print("view this activity's status")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    bottomFrame = LabelFrame(screenMember, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))
    Label(bottomFrame, text = "Activity Status", font = ("new roman", 15)).pack()

    activityInfoFrame = Frame(bottomFrame, padx = 1, pady = 3)
    Label(activityInfoFrame, text = "Club Name:", font = ("new roman", 13)).grid(row = 0, column = 0, sticky = W)
    Label(activityInfoFrame, text = "EECS 391").grid(row = 0, column = 1, sticky = W)
    Label(activityInfoFrame, text = "Activity Name:", font = ("new roman", 13)).grid(row = 1, column = 0, sticky = W)
    Label(activityInfoFrame, text = "Class 5", font = ("new roman", 13)).grid(row = 1, column = 1, sticky = W)

    Label(activityInfoFrame, text = "Activity ID:", font = ("new roman", 13)).grid(row = 2, column = 0, sticky = W)
    Label(activityInfoFrame, text = "123123", font = ("new roman", 13)).grid(row = 2, column = 1, sticky = W)

    Label(activityInfoFrame, text = "Date: ").grid(row = 3, column = 0, sticky = W)
    Label(activityInfoFrame, text = "2020/04/20", font = ("new roman", 13)).grid (row = 3, column = 1, sticky = W)
    Label(activityInfoFrame, text = "Start Time: ", font = ("new roman", 13)).grid(row = 4, column = 0, sticky = W)
    Label(activityInfoFrame, text = "13:00", font = ("new roman", 13)).grid(row = 4, column = 1, sticky = W)
    Label(activityInfoFrame, text = "End Time: ", font = ("new roman", 13)).grid(row = 5, column = 0, sticky = W)
    Label(activityInfoFrame, text = "14:00", font = ("new roman", 13)).grid(row = 5, column = 1, sticky = W)
    Label(activityInfoFrame, text = "Number of Attendees:          ", font = ("new roman", 13)).grid(row = 6, column = 0, sticky = W)
    Label(activityInfoFrame, text = "30", font = ("new roman", 13)).grid(row = 6, column = 1, sticky = W)
    Label(activityInfoFrame, text = "My Check In Time: ", font = ("new roman", 13)).grid(row = 7, column = 0, sticky = W)
    Label(activityInfoFrame, text = "13:04", font = ("new roman", 13)).grid(row = 7, column = 1, sticky = W)
    Label(activityInfoFrame, text = "Present?", font = ("new roman", 13)).grid(row = 8, column = 0, sticky = W)
    Label(activityInfoFrame, text = "Yes", font = ("new roman", 13)).grid(row = 8, column = 1, sticky = W)

    activityInfoFrame.pack()




def deleteClub():
    clicked_items = clubBox.curselection()
    clubBox.delete(clicked_items)
    print("leave club")



def memberManagement():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    frame = Frame(screenAdmin, padx = 10, pady = 10)
    frame.place(x=screen_width/2, y=2, width = screen_width/2, height = screen_height-27)

    Label(frame, text= "Current Members", font = ("new roman", 21)).pack()

    global currentMemberBox
    currentFrame = Frame(frame, padx = 1, pady = 3, height = int(screen_height/5))
    currentScroll = Scrollbar(currentFrame)
    currentScroll.pack(side = RIGHT, fill = Y)
    currentMemberBox = Listbox(currentFrame, yscrollcommand = currentScroll.set, width = int(screen_width/8), height = 7, selectmode = SINGLE)

    #loop for Current Member List
    #while member in MemberList:

    for i in range(1, 15):
        currentMemberBox.insert(END, "LINE " + str(i))

    currentMemberBox.pack(side = LEFT)
    currentScroll.config(command = currentMemberBox.yview)
    currentFrame.pack()

    buttonFrameC = Frame(frame, padx = 1, pady = 3)
    Button(buttonFrameC, text = "Refresh", font = ("new roman", 18), height = 1, width = 9, command = refreshMember).grid(row = 0, column = 0)
    Button(buttonFrameC, text="View", font=("new roman", 18), height=1, width=9, command=viewMember).grid(row=0,
                                                                                                              column=1)
    Button(buttonFrameC, text = "Delete", font = ("new roman", 18), height = 1, width = 9, command = deleteMember).grid(row = 0, column = 2)
    buttonFrameC.pack()

    Label(frame, text = "", font=10).pack()
    Label(frame, text = "Pending Members", font = ("new roman", 21)).pack()

    pendingFrame = Frame(frame, padx = 1, pady = 3)
    pendingScroll = Scrollbar(pendingFrame)
    pendingScroll.pack(side = RIGHT, fill = Y)
    global pendingMemberBox
    pendingMemberBox = Listbox(pendingFrame, yscrollcommand = pendingScroll.set, width = int(screen_width/8), height = 7, selectmode = SINGLE)

    for i in range(1, 15):
        pendingMemberBox.insert(END, "LINE " + str(i))

    pendingMemberBox.pack(side = LEFT)
    pendingScroll.config(command = pendingMemberBox.yview)
    pendingFrame.pack()

    buttonFrameP = Frame(frame, padx = 1, pady=3)
    Button(buttonFrameP, text = "Refresh", font = ("new roman", 18), height = 1, width = 9, command = refreshList).grid(row = 0, column = 0)
    Button(buttonFrameP, text = "Accept", font = ("new roman", 18), height = 1, width = 9, command = acceptMember).grid(row = 0, column = 1)
    Button(buttonFrameP, text = "Reject", font = ("new roman", 18), height = 1, width = 9, command = rejectMember).grid(row = 0, column = 2)
    buttonFrameP.pack()

    bottomFrame = Frame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))



def activityManagement():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    frame = Frame(screenAdmin, padx=10, pady=10)
    frame.place(x=screen_width / 2, y=2, width=screen_width / 2, height=screen_height-27)
    Label(frame, text = "Activities", font = ("new roman", 21)).pack()

    global activityBox
    activityFrame = Frame(frame, padx = 1, pady = 3, height = int(screen_height / 2))
    activityScroll = Scrollbar(activityFrame)
    activityScroll.pack(side = RIGHT, fill = Y)
    activityBox = Listbox(activityFrame, yscrollcommand = activityScroll.set, width = int(screen_width/8), height = 19, selectmode = SINGLE)

    for i in range(1, 20):
        activityBox.insert(END, "LINE " + str(i))

    activityBox.pack(side = LEFT)
    activityScroll.config(command = activityBox.yview)
    activityFrame.pack()

    buttonFrameA = Frame(frame, padx = 0, pady=3)
    Button(buttonFrameA, text = "Refresh", font = ("new roman", 18), height = 1, width = 7, command = refreshActivity).grid(row = 0, column = 0)
    Button(buttonFrameA, text = "View", font = ("new roman", 18), height = 1, width = 6, command = viewActivity).grid(row = 0, column = 1)
    Button(buttonFrameA, text = "Create", font = ("new roman", 18), height = 1, width = 7, command = createActivity).grid(row = 0, column = 2)
    Button(buttonFrameA, text = "Delete", font = ("new roman", 18), height = 1, width = 7, command = deleteActivity).grid(row = 0, column = 3)
    buttonFrameA.pack()

    bottomFrame = Frame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))

def deleteActivity():
    print("delete activity")


def refreshActivity():
    print("refresh activity")


def updateTime():
    print("update time")
    global updateTimeScreen
    updateTimeScreen = Toplevel(screen)
    updateTimeScreen.title("Update Activity Information")
    updateTimeScreen.geometry("400x400+30+30")
    Label(updateTimeScreen, text = "").pack()
    Label(updateTimeScreen, text = "New Date", font = ("new roman", 15)).pack()
    date_entry = Entry(updateTimeScreen)
    date_entry.pack()
    Label(updateTimeScreen, text="").pack()
    Label(updateTimeScreen, text = "New Start Time", font = ("new roman", 15)).pack()
    starttime_entry = Entry(updateTimeScreen)
    starttime_entry.pack()
    Label(updateTimeScreen, text="").pack()
    Label(updateTimeScreen, text = "New End Time", font = ("new roman", 15)).pack()
    endtime_entry = Entry(updateTimeScreen)
    endtime_entry.pack()
    Label(updateTimeScreen, text = "").pack()
    Label(updateTimeScreen, text = "Location", font = ("new roman", 15)).pack()
    location_entry = Entry(updateTimeScreen)
    location_entry.pack()
    Label(updateTimeScreen, text="").pack()

    #global newMemberBox
    #newMemberFrame = Frame(updateTimeScreen, padx = 1, pady = 3, height = 100, width = 200)
    #newMemberScroll = Scrollbar(newMemberFrame)
    #newMemberScroll.pack(side = RIGHT, fill = Y)
    #newMemberBox = Listbox(newMemberFrame, yscrollcommand = newMemberScroll.set, width = 200, height = 4, selectmode = MULTIPLE)

    #for i in range(1, 20):
    #   newMemberBox.insert(END, "LINE " + str(i))

    #newMemberBox.pack(side = LEFT)
    #newMemberScroll.config(command = newMemberBox.yview)
    #newMemberFrame.pack()

    Button(updateTimeScreen, text = "Update Information", font = ("new roman", 15), height = 2, width = 20, command = updateTimeInfo).pack()


def updateTimeInfo():
    print("update activity time information")



def refreshActivityInfo():
    print("refresh activity info, including member list and time")


def viewActivity():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    bottomFrame = LabelFrame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))
    Label(bottomFrame, text = "Activity Status", font = ("new roman", 15)).pack()

    timeFrame = Frame(bottomFrame, padx = 1, pady = 3)
    Label(timeFrame, text = "Date", font = ("new roman", 13)).grid (row = 0, column = 0)
    Label(timeFrame, text = "2020/04/04", font = ("new roman", 13)).grid(row = 1, column = 0)
    Label(timeFrame, text = "Start Time", font = ("new roman", 13)).grid(row = 0, column = 1)
    Label(timeFrame, text = "  ").grid(row = 0, column = 2)
    Label(timeFrame, text = "End Time", font = ("new roman", 13)).grid(row = 0, column = 3)
    #pull out information about the start time and end time
    Label(timeFrame, text = "12:00", font = ("new roman", 13)).grid(row = 1, column = 1)
    Label(timeFrame, text = "  ").grid(row = 1, column = 2)
    Label(timeFrame, text = "14:00", font = ("new roman", 13)).grid (row = 1, column = 3)
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
    memberid_entry = Entry(leftFrame, width = 25)
    memberid_entry.grid(row = 1, column = 0, sticky = W)
    Button(leftFrame, text = "OK", font = ("new roman", 15), command = getMemberPhoto).grid(row = 1, column = 1)
    Label(leftFrame, text = "").grid(row = 2, column = 0)


    rightFrame = Frame(screenAttendance, padx = 10, pady = 10)
    rightFrame.place(x = screen_width / 2, y = 2, width = screen_width/2, height = int(screen_height*2/3))
    Label(rightFrame, text = "Camera", font = ("new roman", 15)).grid(row = 0, column = 0, sticky = W)
    cameraFrame = LabelFrame(rightFrame, padx= 10, pady = 10, width = screen_width/3 + 20, height = screen_width/3+ 20)
    cameraFrame.grid(row = 1, column = 0)

    Button(screenAttendance, text = "Attend", font = ("new roman", 15), height = 2, width = 20, command = attend).place(x = 10, y = int (screen_height*2/3) + 30)
    Button(screenAttendance, text = "Verify", font = ("new roman", 15), height = 2, width = 20, command = takePhoto).place(
        x = screen_width/2+10, y = int(screen_height*2/3)+30)

def takePhoto():
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
    Label(screenReport, text = "").grid(row = 0, column = 0)
    Label(screenReport, text = "Activity Name: ", font = ("new roman", 15)).grid(row = 1, column = 0, sticky = W)
    Label(screenReport, text = "Class 5", font = ("new roman", 15)).grid(row = 1, column = 1, sticky = W)
    Label(screenReport, text = "Number of Attendees:     ", font = ("new roman", 15)).grid(row = 2, column = 0, sticky = W)
    Label(screenReport, text = "30", font = ("new roman", 15)).grid(row = 2, column = 1, sticky = W)
    Label(screenReport, text = "Number of Attended: ", font = ("new roman", 15)).grid(row = 3, column = 0, sticky = W)
    Label(screenReport, text = "15", font = ("new roman", 15)).grid(row = 3, column = 1, sticky = W)
    Label(screenReport, text = "Number of Absenses: ", font = ("new roman", 15)).grid(row = 4, column = 0, sticky = W)
    Label(screenReport, text = "15", font = ("new roman", 15)).grid(row = 4, column = 1, sticky = W)
    Label(screenReport, text = "Attendance Rate", font = ("new roman", 15)).grid(row = 5, column = 0, sticky = W)
    Label(screenReport, text="50", font=("new roman", 15)).grid(row=5, column=1, sticky=W)


def createActivity():
    print("create activity")
    global screenCreateActivity
    screenCreateActivity = Toplevel(screenAdmin)
    screenCreateActivity.title("New Activity")
    screenCreateActivity.geometry("400x750+10+10")
    # 1
    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Activity ID").pack()
    activity_entry = Entry(screenCreateActivity)
    activity_entry.pack()

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

    Label(screenCreateActivity, text = "").pack()
    Label(screenCreateActivity, text = "Location").pack()
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
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2

    global screenAdmin
    screenAdmin = Frame(screen, width = screen_width, height = screen_height)
    screenAdmin.grid(row = 0, column = 0)
    screen.title("Administrator")

    xCoor = screen_width /2
    yCoor = screen_height / 2
    #screenAdmin.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor,yCoor))

    leftFrame = Frame(screenAdmin, padx = 10, pady = 10)
    leftFrame.place(x = 0, y = 2, width = screen_width/2, height = screen_height/3)
    Button(leftFrame, text = "Member Management", font = ("new roman", 20), height = 2, width = 25, command = memberManagement).grid(row = 0, column = 0)
    Label(leftFrame, text = "", height = 1, width = 25).grid(row = 1, column = 0)
    Button(leftFrame, text = "Activity Management", font = ("new roman", 20), height = 2, width = 25, command = activityManagement).grid(row = 2, column = 0)

    Button(screenAdmin, text = "Log out", font = ("new roman", 13), command = lambda:raise_frame(login_page)).place(x = screen_width - 70, y = screen_height - 25)
    # command = lambda:raise_frame(login_page)
    memberManagement()


def viewMember():
    clicked_items = currentMemberBox.curselection()

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    bottomFrame = LabelFrame(screenAdmin, padx = 10, pady = 5)
    bottomFrame.place(x = 5, y = screen_height/3+2, width = screen_width/2-5, height = int(screen_height*2/3 - 10))
    Label(bottomFrame, text = "Member Status", font = ("new roman", 15)).pack()

    infoFrame = Frame(bottomFrame, padx = 1, pady = 3)
    Label(infoFrame, text = "Name: ", font = ("new roman", 13)).grid(row = 0, column = 0, sticky = W)
    Label(infoFrame, text = "Han Pi", font = ("new roman", 13)).grid(row = 0, column = 1, sticky = W)
    Label(infoFrame, text = "ID: ", font = ("new roman", 13)).grid(row = 1, column = 0, sticky = W)
    Label(infoFrame, text = "hxp342", font = ("new roman", 13)).grid(row = 1, column = 1, sticky = W)
    Label(infoFrame, text = "Email: ", font = ("new roman", 13)).grid(row = 2, column = 0, sticky = W)
    Label(infoFrame, text = "hxp342@case.edu", font = ("new roman", 13)).grid (row = 2, column = 1, sticky = W)
    Label(infoFrame, text = "Attendance Rate:    ", font = ("new roman", 13)).grid(row = 3, column = 0, sticky = W)
    Label(infoFrame, text = "50", font = ("new roman", 13)).grid(row = 3, column = 1, sticky = W)
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





def rejectMember():
    clicked_items = pendingMemberBox.curselection()
    pendingMemberBox.delete(clicked_items)


def acceptMember():
    clicked_items = pendingMemberBox.curselection()
    #print(pendingMemberBox.get(clicked_items))
    currentMemberBox.insert(END, currentMemberBox.get(clicked_items))
    pendingMemberBox.delete(clicked_items)
    print("pending member is added to the current member list")

def deleteMember():
    clicked_items = currentMemberBox.curselection()
    currentMemberBox.delete(clicked_items)



def refreshMember():
    print("Refresh current member list")


def refreshList():
    print("Refresh pending member list")



def forget():
    print("U SUCK")


main_screen()
