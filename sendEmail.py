import smtplib, ssl
import pymsgbox as pgbox
import tkinter as tk
import re

def construct_email(e1, e2, smtp_server, sender, receiver, password, port, name, id, master):
    message = """\
                From: %s
                \nTo: %s
                \nSubject: %s
                \n%s
                """ % (sender, receiver, ('[Received Request From: %s] ' %id) + e1.get(), ('Hello, this is %s. \n' %name) + e2.get('1.0', 'end'))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.ehlo()  # Can be omitted
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.close()
    tk.Label(master, text="Email sent successfully").grid(column=0, row=4, sticky=tk.W)

def send_email(sender_email: str, sender_password: str, receiver_email: str, sder_name: str, sder_id: str):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    if(valid_email_addr(sender_email) and valid_email_addr(receiver_email)):
        sender = sender_email
        receiver = receiver_email
    password = sender_password

    master = tk.Tk()
    master.title("Send Email Notification")
    master.geometry("600x300")
    tk.Label(master, text="Subject: ").grid(row=0)
    tk.Label(master, text="Notification: ").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Text(master, width=60, height=10)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master,
              text='Cancel',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master,
              text='Confirm', command=lambda : construct_email(e1, e2, smtp_server, sender, receiver, password, port, sder_name, sder_id, master)).grid(row=3,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)
    master.mainloop()

def valid_email_addr(email_addr: str) -> bool:
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(regex, email_addr)):
        return True
    else:
        pgbox.alert('Invalid Email Address %s' %email_addr, 'Alert');
        return False