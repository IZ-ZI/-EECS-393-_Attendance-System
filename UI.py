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

currentMemberBox = None
currentScroll = None
currentFrame = None
buttonFrameC = None

pendingMemberBox = None
pendingFrame = None
pendingScroll = None
buttonFrameP = None

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

    # new_member.requestPermission(administrator)

    administrator.pend_member(new_member)

    member_id_entry.delete(0, END)
    member_name_entry.delete(0, END)
    member_email_entry.delete(0, END)
    member_password_entry.delete(0, END)
    member_confirm_password_entry.delete(0, END)
    member_apply_club_id_entry.delete(0, END)

    member_register_feedback['text'] = 'Registration Success'


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
    Label(screen, text="Club/Organization ID", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height / 30)
    Label(screen, text="Password", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height * 10 / 30)
    Button(screen, text="New Club Register", height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Administrator Login", font=("new roman", 15), height="5", width="20", command=admin_login,
           fg='black').place(x=screen_width / 30, y=screen_height * 2 / 3)


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

        Label(frame, text="Clubs", font=("new roman", 21)).pack()
        clubFrame = Frame(frame, padx=1, pady=3, height=int(screen_height / 5))
        clubScroll = Scrollbar(clubFrame)
        clubScroll.pack(side=RIGHT, fill=Y)
        clubBox = Listbox(clubFrame, yscrollcommand=clubScroll.set, width=int(screen_width / 8), height=20,
                          selectmode=SINGLE)

        for i in range(1, 15):
            clubBox.insert(END, "LINE " + str(i))

        clubBox.pack(side=LEFT)
        clubScroll.config(command=clubBox.yview)
        clubFrame.pack()


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

        showCurrentMember(frame, logged_admin)

        currentMemberBox.pack(side=LEFT)
        currentScroll.config(command=currentMemberBox.yview)
        currentFrame.pack()

        buttonFrameC = Frame(frame, padx=1, pady=3)
        Button(buttonFrameC, text="Refresh", font=("new roman", 18), height=1, width=9,
               command=lambda: refreshMember(frame, logged_admin)).grid(
            row=0, column=0)

        Button(buttonFrameC, text = "View", font = ("new roman", 18), height = 1, width = 9, command = viewMember).grid(row = 0, column = 1)

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
               command=lambda: refreshList(frame, logged_admin)).grid(row=0,
                                                                      column=0)
        Button(buttonFrameP, text="Accept", font=("new roman", 18), height=1, width=9, command=lambda:acceptMember(frame, logged_admin)).grid(row=0,
                                                                                                                  column=1)
        Button(buttonFrameP, text="Reject", font=("new roman", 18), height=1, width=9, command=lambda:rejectMember(frame, logged_admin)).grid(row=0,
                                                                                                                  column=2)
        buttonFrameP.pack()

        showPendingMember(frame, logged_admin)


def showPendingMember(frame, logged_admin):
    global pendingMemberBox
    global pending_member_list
    for i in logged_admin.get_member_database().wait_list:
        if(i not in pending_member_list):
            pending_member_list.append(i)
            pendingMemberBox.insert(END,  "ID: " + i.get_id() + "  " + "Name: " + i.get_name())



def showCurrentMember(frame, logged_admin):
    # loop for Current Member List
    # while member in MemberList:
    global currentMemberBox
    global current_member_list
    for i in logged_admin.get_member_database().database:
        if(i not in current_member_list):
            current_member_list.append(i)
            currentMemberBox.insert(END,  "ID: " + i.get_id() + "  " + "Name: " + i.get_name())



def rejectMember(frame, logged_admin):
    global pending_member_list
    if pendingMemberBox.curselection() != ():
        clicked_item_index = pendingMemberBox.curselection()[0]
        rej_id = logged_admin.get_member_database().wait_list[clicked_item_index].get_id()
        logged_admin.get_member_database().reject_pending_member(rej_id)
        pendingMemberBox.delete(clicked_item_index)
        pending_member_list.remove(logged_admin.get_member_database().wait_list[clicked_item_index])
        refreshList(frame, logged_admin)


def acceptMember(frame, logged_admin):
    if pendingMemberBox.curselection() != ():
        clicked_item_index = pendingMemberBox.curselection()[0]
        acc_id = logged_admin.get_member_database().wait_list[clicked_item_index].get_id()
        logged_admin.get_member_database().permit_pending_member(acc_id)
        pendingMemberBox.delete(clicked_item_index)
        refreshList(frame, logged_admin)
        refreshMember(frame, logged_admin)


def deleteMember():
    clicked_items = currentMemberBox.curselection()
    currentMemberBox.delete(clicked_items)


def refreshMember(frame, logged_admin):
    showCurrentMember(frame,logged_admin)


def refreshList(frame, logged_admin):
    showPendingMember(frame, logged_admin)

def viewMember():
    clicked_items = currentMemberBox.curselection()
    memberInfo = Toplevel(screenAdmin)
    name = None  #fill in member name
    memberInfo.title("Member " + name + " Information")
    memberInfo.geometry("100x100")


def member():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="User ID                              ", font=("new roman", 20)).place(x=screen_width / 30,
                                                                                              y=screen_height / 30)
    Button(screen, text="New Member Register", height="5", width="20", command=member_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Member Login", font=("new roman", 15), height="5", width="20", command=member_login,
           fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)

def display_password():
    if(show_password.get()):
        login_password_entry.config(show="")
    else:
        login_password_entry.config(show="*")

def login():
    print("Login session started")


def forget():
    print("U SUCK")


main_screen()
