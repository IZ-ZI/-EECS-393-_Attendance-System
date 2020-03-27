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


screenAdmin  = None

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

administrator_list = None
member_list = None

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

    login_account = StringVar()
    login_password = StringVar()

    Label(screen, text="Club/Organization ID", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height / 30)

    # member_email_entry = Entry(screen1, textvariable=member_email)

    login_account_entry = Entry(screen, textvariable=login_account, width="20")
    login_account_entry.place(x=screen_width / 30, y=screen_height * 3 / 30)

    Label(screen, text="Password", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height * 10 / 30)

    login_password_entry = Entry(screen, textvariable=login_password, width="20")
    login_password_entry.place(x=screen_width / 30, y=screen_height * 13 / 30)

    # highlightbackground = 'green'

    Button(screen, text="Administrator", height="5", width="20", command=admin, fg='black').place(
        x=screen_width * 2 / 3, y=screen_height / 30)
    Button(screen, text="Member", height="5", width="20", command=member, fg='black', ).place(x=screen_width * 2 / 3,
                                                                                              y=screen_height / 4 + screen_height / 30)

    Button(screen, text="Login", height="5", width="20", command=admin_login, fg='black').place(x=screen_width / 30,
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
    global club_password #do this

    if(club_password.get() != club_confirm_password.get()):
        club_register_feedback['text'] = 'Password difference'
        # club_register_feedback.set("Password Difference")
    elif(club_id.get() =='' or club_name.get()=='' or club_email.get()==''  or club_password.get()=='' or club_confirm_password.get() ==''):
        club_register_feedback['text'] = 'Please fill all the spaces'
    else:
        club_info()

def member_register_check():
    if(member_password.get() != member_confirm_password.get()):
        member_register_feedback['text'] = 'Password difference'
    elif(member_id.get() =='' or member_name.get()=='' or member_email.get()==''  or member_password.get()=='' or member_confirm_password.get() =='' or member_apply_club_id.get() ==''):
        member_register_feedback['text'] = 'Please fill all the spaces'
    else:
        member_info()

def club_info():
    #file = open(club_id.get() + ".txt", "w")
    #file.write(club_id.get() + "\n")
    #file.write(club_name.get() + "\n")
    #file.write(club_email.get() + "\n")
    #file.write(club_password.get() + "\n")
    #file.write(club_confirm_password.get() + "\n")
    #file.close()
    administrator = Administrator(club_name.get(), club_id.get(), club_email.get(), club_password.get())
    administrator_list.append(administrator)


    club_id_entry.delete(0, END)
    club_name_entry.delete(0, END)
    club_email_entry.delete(0, END)
    club_password_entry.delete(0, END)
    club_confirm_password_entry.delete(0, END)

    club_register_feedback['text'] = 'Registration sent'


def id_to_admin(id):
    global administrator_list
    for i in administrator_list:
        if i.get_organization_id == id:
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

    new_member = Administrator(member_name.get(), member_id.get(), member_email.get(), member_password.get())
    member_list.append(new_member)

    #this send email to club by using member_apply_club_id

    administrator = id_to_admin(member_apply_club_id.get())

    administrator.pend_member(new_member)



    member_id_entry.delete(0,END)
    member_name_entry.delete(0,END)
    member_email_entry.delete(0,END)
    member_password_entry.delete(0,END)
    member_confirm_password_entry.delete(0,END)
    member_apply_club_id_entry.delete(0,END)

    member_register_feedback['text'] = 'Registration sent'

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
    member_password_entry = Entry(screen1, textvariable=member_password)
    member_password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    member_confirm_password_entry = Entry(screen1, textvariable=member_confirm_password)
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
    Label(screen1, text = "").pack()
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
    club_password_entry = Entry(screen1, textvariable=club_password)
    club_password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    club_confirm_password_entry = Entry(screen1, textvariable=club_confirm_password)
    club_confirm_password_entry.pack()

    # 6
    Label(screen1, text = "").pack()
    Button(screen1, text="Register", height= "3", width = "20", command = club_register_check).pack()

    # 7
    Label(screen1, text = "").pack()
    club_register_feedback = Label(screen1, text=" ", fg="green", font=("new roman", 15))
    club_register_feedback.pack()


def admin():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="Club/Organization ID", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height / 30)
    Label(screen, text="Password",font=("new roman", 20)).place(x=screen_width / 30, y=screen_height*10/30)
    Button(screen, text="New Club Register", height="5", width="20", command=club_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Administrator Login", font = ("new roman", 15),height= "5", width = "20", command = admin_login, fg='black').place(x = screen_width/30, y = screen_height*2/3)


def member_login():
    global screenMember
    print("member login session started")
    print('%s' %login_account_entry)
    # implement whatever needed to check for login
    if member_id != '' and member_password:
        if login_account_entry == member_id and login_password_entry == member_password:
               screenMember = Toplevel(screen)
               screenMember.title("Member")
               screen_width = screen.winfo_screenwidth() / 2
               screen_height = screen.winfo_screenheight() / 2
               xCoor = screen_width / 2 + 20
               yCoor = screen_height / 2 + 20

               screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))

    else:
        print('error')
        screenMember = Toplevel(screen)
        screenMember.title("Error")
        screen_width = screen.winfo_screenwidth() / 8
        screen_height = screen.winfo_screenheight() / 8
        xCoor = screen_width / 2 + 20
        yCoor = screen_height / 2 + 20

        screenMember.geometry("%dx%d+%d+%d" % (screen_width, screen_height, xCoor, yCoor))

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
    frame = LabelFrame(screenAdmin, text = "Members", font = ("new roman", 21), padx = 10, pady = 10, height = screen_height, width = screen_width/2)
    frame.place(x=screen_width/2, y=0)

    Label(frame, text= "Current Members", font = ("new roman", 21)).pack()

    Button(frame, text = "Refresh Members", font = ("new roman", 15), command = refreshMember).pack()

    Label(frame, text = "Pending Members", font = ("new roman", 21)).pack()
    Button(frame, text = "Refresh List", font = ("new roman", 15), command = refreshList).pack()


def refreshMember():
    print("Refresh current member list")


def refreshList():
    print("Refresh pending member list")

def member():
    screen_width = screen.winfo_screenwidth() / 2
    screen_height = screen.winfo_screenheight() / 2
    Label(screen, text="User ID                              ", font=("new roman", 20)).place(x=screen_width / 30, y=screen_height / 30)
    Button(screen, text="New Member Register", height="5", width="20", command=member_register, fg='black').place(
        x=screen_width * 2 / 3 + screen_width / 30, y=screen_height * 2 / 3)
    Button(screen, text="Member Login", font = ("new roman", 15),height="5", width="20", command=member_login, fg='black').place(
        x=screen_width / 30, y=screen_height * 2 / 3)


def login():
    print("Login session started")


def forget():
    print("U SUCK")


main_screen()
