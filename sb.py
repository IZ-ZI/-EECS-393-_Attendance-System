# print("脑瘫睿智女对战暗黑战神")
# print("脑瘫睿智女对战暗黑战神")
# print("脑瘫睿智女对战暗黑战神")
# print(4321)


from tkinter import *

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x400")
    screen.title("Attendance System Login")

    # Label(text= "Note",bg="grey",font=("new roman", 15)).pack()
    Label(screen, text="IDENTITY", bg= "grey", width = "600", height= "2", font=("new roman", 15)).pack()
    Label(screen, text="").pack()
    Label(screen, text="Username:", width = "20", height= "2", font=("new roman", 15)).pack()
    Entry(screen).pack()

    Label(screen, text="").pack()
    Label(screen, text="Password:",  width = "20", height= "2", font=("new roman", 15)).pack()
    Entry(screen).pack()

    Label(screen, text="").pack()
    Label(screen, text="").pack()

    Button(screen, text="Login", height= "3", width = "20", command = login).pack()
    Button(screen, text="Register", height= "3", width = "20", command = register).pack()

    screen.mainloop()




def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(screen1, text = "Registration sent", fg = "green", font=("new roman", 15)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x400")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Username").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password").pack()

    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    Label(screen1, text = "").pack()
    Button(screen1, text="Register", height= "3", width = "20", command = register_user).pack()


def login():
    print("Login session started")



main_screen()