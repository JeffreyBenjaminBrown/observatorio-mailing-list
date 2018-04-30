# references
  # email generally: https://docs.python.org/3/library/email.examples.html
  # attachments: https://stackoverflow.com/questions/26582811/gmail-python-multiple-attachments

import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders as Encoders


def main():
  user =     open("private/credentials/user.txt")    .read().strip()
  password = open("private/credentials/password.txt").read().strip()

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login(user, password)

  msg = MIMEMultipart()
  msg['Subject'] = 'Latest subscriptions to email list. Automated email.'
  msg['To'] = "ofiscalpuj" + "@gmail.com"
  msg['From'] = user       + "@gmail.com"

  for file in [ "private/output/addresses.txt"
              , "private/output/active_subscriptions.csv"]:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
    msg.attach(part)

  server.send_message(msg)
  server.quit()
