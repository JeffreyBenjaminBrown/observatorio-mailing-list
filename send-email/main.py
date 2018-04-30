# https://docs.python.org/3/library/email.examples.html

import smtplib
from email.message import EmailMessage


user = open("send-email/user.txt").read().strip()
password = open("send-email/password.txt").read().strip()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(user, password)

msg = EmailMessage()
msg['Subject'] = 'Test mail'
msg['To'] = user + "@gmail.com"
msg['From'] = user + "@gmail.com"
msg.set_payload( open("private/output/addresses.txt").read(), charset = 'utf-8')

server.send_message(msg)
server.quit()
