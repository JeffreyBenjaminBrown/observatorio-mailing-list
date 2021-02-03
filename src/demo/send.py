import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders as Encoders


def main():
  sender     = open("private/sender")    .read() .strip()
    # A plain text file with no extraneous space or newline.
  password   = open("private/password")  .read() .strip()
    # A plain text file with no extraneous space or newline.
  recipients = " ".join(
      [sender, "nobody@does_not_exist.com" ] )
  #
  server = smtplib . SMTP ('smtp.gmail.com', 587)
  server . ehlo ()
  server . starttls ()
  server . login (sender, password)
  #
  msg = MIMEMultipart ()
  msg [ 'Subject' ] = "Testing, testing ..."
  msg [ 'To' ] = recipients
  msg [ 'From' ] = sender
  #
  for file in []: # add some attachments
    part = MIMEBase ( 'application', 'octet-stream' )
    part . set_payload ( open ( file, 'rb' )
                         . read () )
    Encoders . encode_base64 ( part )
    part . add_header(
        'Content-Disposition',
        'attachment; filename="%s"' % file)
    msg . attach ( part )
  #
  server . send_message ( msg )
  server . quit ()
