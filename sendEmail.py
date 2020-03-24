import smtplib, ssl
import pymsgbox as pgbox
import re

def send_email(sender_email: str, sender_password: str, receiver_email: str):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    if(valid_email_addr(sender_email) and valid_email_addr(receiver_email)):
        sender = sender_email
        receiver = receiver_email
    password = sender_password
    message = """\
    Subject: Message Subject
    
    Message Body."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

def valid_email_addr(email_addr: str) -> bool:
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(regex, email_addr)):
        return True
    else:
        pgbox.alert('Invalid Email Address %s' %email_addr, 'Alert');
        return False


