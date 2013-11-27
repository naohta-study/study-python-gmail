# -*- coding: utf-8 -*-
# http://unoh.github.io/2007/06/13/python_2.html
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
import sys

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send_via_gmail(from_addr, from_pswd, to_addr, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo
    s.login(from_addr, from_pswd)
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.close()

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print sys.argv
        print 'python-gmail.py from_addr from_pswd to_addr subject body'
        sys.exit()
    from_addr = sys.argv[1]
    from_pswd = sys.argv[2]
    to_addr = sys.argv[3]
    subject = sys.argv[4]
    body = sys.argv[5]
    msg = create_message(from_addr, to_addr, subject, body)
    send_via_gmail(from_addr, from_pswd, to_addr, msg)

