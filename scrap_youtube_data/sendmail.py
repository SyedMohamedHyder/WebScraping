import os.path
import smtplib
import mimetypes
from getpass import getpass
from email.message import EmailMessage

class SendMail:
    def __init__(self, sender, reciever):
        self.sender = sender
        self.reciever = reciever
        self.message = EmailMessage()
        self.message['From'] = self.sender
        self.message['To'] = self.reciever

    def add_subject(self, subject):
        self.message['Subject'] = subject

    def add_body(self, body):
        self.message.set_content(body)

    def add_attachment(self, filename):
        filepath = os.path.abspath(filename)
        mimetype, _ = mimetypes.guess_type(filepath)
        mimetype, subtype = mimetype.split('/', 1)
        with open(filepath, 'rb') as file:
            self.message.add_attachment(file.read(),
                                   maintype=mimetype,
                                   subtype=subtype,
                                   filename=filename)

    def send(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            password = getpass('Enter your password : ')
            print('Loging in')
            server.login(self.sender, password)
            print('Sending mail')
            server.sendmail(self.sender, self.reciever, self.message.as_string())
            print('Mail sent')
        finally:
            server.quit()
            print('Closed the server')
