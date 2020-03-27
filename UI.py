from tkinter import *

def main_screen():
    global screen
    screen = Tk()
    #screen.geometry("600x300")
    screen.title("Attendance System Login")
    # screen.configure(background='turquoise')

    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    xCoor = screen_width /2
    yCoor = screen_height / 2

    screen.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor,yCoor))

    Label(screen, text="Club/Organization ID", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height*2 / 30)
    Entry(screen,width = "30").place(x=screen_width / 24, y=screen_height * 5/30)
    Label(screen, text="Password",font=("new roman", 21)).place(x=screen_width/24, y=screen_height*10/30)
    Entry(screen,width = "30").place(x = screen_width / 24, y= screen_height*13/30)

    # highlightbackground = 'green'

    Button(screen, text="Administrator", font = ("new roman", 15), height="5", width="20", command = admin, fg='black', ).place(x=screen_width*6.5/10, y=screen_height/25)
    Button(screen, text="Member", font = ("new roman", 15),height= "5", width ="20", command = member, fg='black', ).place(x = screen_width *6.5/10, y = screen_height/4+screen_height/30)

    Button(screen, text="Administrator Login",font = ("new roman", 15), height= "5", width = "20", command = admin_login, fg='black').place(x = screen_width/30, y = screen_height*2/3)
   # Button(screen, text="Login", height= "3", width = "20", command = login, fg='black').grid(row=6, column=0)
    Button(screen, text="Forget/Reset Password", font = ("new roman", 15),height= "5", width = "20", command = forget, fg='black').place(x=screen_width/3 + screen_width/30, y=screen_height*2/3)

    Button(screen, text="New Club Register", font = ("new roman", 15),height= "5", width = "20", command = club_register, fg='black').place(x=screen_width*2/3+screen_width/30, y=screen_height*2/3)


    # global button
    # button = Button(screen,text='Submit',command=changeText)
    # button.pack()

    screen.mainloop()

# def changeText():
#     if (button['text'] == 'Submit'):
#         button['text'] = 'Submitted'
#     else:
#         button['text'] = 'Submit'

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
   # Label(screen, text="Password",font=("new roman", 21)).place(x=screen_width / 24, y=screen_height*10/30)
    Button(screen, text="New Club Register", font = ("new roman", 15),height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Administrator Login", font = ("new roman", 15),height= "5", width = "20", command = admin_login, fg='black').place(x = screen_width/30, y = screen_height*2/3)
def member():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="User ID                            ", font=("new roman", 21)).place(x=screen_width / 24, y=screen_height * 2/ 30)
    #Label(screen, text = "", height = 2, width = 30).place(x=screen_width* 2.1 /15, y = screen_height *2/30)
    Button(screen, text="New Member Register", font = ("new roman", 15),height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Member Login", font = ("new roman", 15),height="5", width="20", command=member_login, fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)


def member_login():
    print("member login session started")
    #implement whatever needed to check for login
    global screenMember
    screenMember = Toplevel(screen)
    screenMember.title("Member")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    xCoor = screen_width /2+20
    yCoor = screen_height / 2+20
    screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor,yCoor))

    frame = Frame(screenMember, padx = 10, pady = 10)
    frame.place(x=screen_width/2, y=2, width = screen_width/2, height = screen_height)

    Label(frame, text = "Clubs", font = ("new roman", 21)).pack()
    clubFrame = Frame(frame, padx= 1, pady = 3, height = int(screen_height / 5))
    clubScroll = Scrollbar(clubFrame)
    clubScroll.pack(side = RIGHT, fill = Y)
    clubBox = Listbox(clubFrame, yscrollcommand = clubScroll.set, width = int(screen_width/8), height = 20, selectmode = SINGLE)

    for i in range(1, 15):
        clubBox.insert(END, "LINE " + str(i))

    clubBox.pack(side = LEFT)
    clubScroll.config(command = clubBox.yview)
    clubFrame.pack()





def admin_login():
    print("admin login session started")
    #implement whatever needed to check for login

    global screenAdmin
    screenAdmin = Toplevel(screen)
    screenAdmin.title("Administrator")
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    xCoor = screen_width /2
    yCoor = screen_height / 2
    screenAdmin.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor,yCoor))

    frame = Frame(screenAdmin, padx = 10, pady = 10)
    frame.place(x=screen_width/2, y=2, width = screen_width/2, height = screen_height)


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

    buttonFrame = Frame(frame, padx = 1, pady = 3)
    Button(buttonFrame, text = "Refresh", font = ("new roman", 18), height = 1, width = 13, command = refreshMember).grid(row = 0, column = 0)
    Button(buttonFrame, text = "Delete", font = ("new roman", 18), height = 1, width = 13, command = deleteMember).grid(row = 0, column = 1)
    buttonFrame.pack()

    Label(frame, text = "", font=10).pack()
    Label(frame, text = "Pending Members", font = ("new roman", 21)).pack()

    pendingFrame = Frame(frame, padx = 1, pady = 3)
    pendingScroll = Scrollbar(pendingFrame)
    pendingScroll.pack(side = RIGHT, fill = Y)
    pendingMemberBox = Listbox(pendingFrame, yscrollcommand = pendingScroll.set, width = int(screen_width/8), height = 7, selectmode = SINGLE)

    for i in range(1, 15):
        pendingMemberBox.insert(END, "LINE " + str(i))

    pendingMemberBox.pack(side = LEFT)
    pendingScroll.config(command = pendingMemberBox.yview)
    pendingFrame.pack()
    Button(frame, text = "Refresh List", font = ("new roman", 18), height = 1, width = 20, command = refreshList).pack()



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
