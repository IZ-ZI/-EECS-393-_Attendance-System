from tkinter import *

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x300")
    screen.title("Attendance System Login")
    # screen.configure(background='turquoise')

    Label(screen, text="Club/Organization ID", width = "20", height= "2", font=("new roman", 15)).grid(row=1,column=0)
    Entry(screen,width = "20").grid(row=2, column=0)
    Label(screen, text="Password",  width = "20", height= "2", font=("new roman", 15)).grid(row=3)
    Entry(screen,width = "20").grid(row=4, column=0)
    Label(screen, text="").grid(row=5)

    # highlightbackground = 'green'
    Button(screen, text="Login", height= "3", width = "20", command = login, fg='black').grid(row=6, column=0)


    Button(screen, text="Administrator", height= "3", width = "20", command = admin, fg='black', ).grid(row=2, column=2)
    Button(screen, text="Member", height= "3", width = "20", command = member, fg='black', ).grid(row=3, column=2)


    Button(screen, text="Login", height= "3", width = "20", command = login, fg='black').grid(row=6, column=0)
    Button(screen, text="Forget/Reset Password", height= "3", width = "20", command = forget, fg='black').grid(row=6, column=1)

    Button(screen, text="New Club Register", height= "3", width = "20", command = club_register, fg='black').grid(row=6, column=2)


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
    Label(screen, text="Club/Organization ID", width = "20", height= "2", font=("new roman", 15)).grid(row=1,column=0)
    Label(screen, text="Password",  width = "20", height= "2", font=("new roman", 15)).grid(row=3)
    Button(screen, text="New Club Register", height= "3", width = "20", command = club_register, fg='black').grid(row=6, column=2)


def member():
    Label(screen, text="User ID", width = "20", height= "2", font=("new roman", 15)).grid(row=1,column=0)
    Button(screen, text="New Member Register", height= "3", width = "20", command = member_register, fg='black').grid(row=6, column=2)


def login():
    print("Login session started")

def forget():
    print("U SUCK")


main_screen()