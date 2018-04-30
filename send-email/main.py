# Adapted from https://gist.github.com/yzhong52/d703ec82aeee24164f0c

import smtplib


# This is a little redundant because ...
user = open("send-email/user.txt").read().strip()
password = open("send-email/password.txt").read().strip()


# ... I'm trying to minimize changes to the code below from yzhong52 at all
TO = user + "@gmail.com"
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

gmail_sender = TO
gmail_passwd = password

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
