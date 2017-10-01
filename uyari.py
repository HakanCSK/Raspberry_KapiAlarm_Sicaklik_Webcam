#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os
from ayar import *
from derece import *



def sendMail(to, subject, text):
    assert type(to)==list


    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject + kapi

    msg.attach( MIMEText(text) )



    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, to, msg.as_string())
    server.quit()
if temperature>23:
   sendMail( ["coskunhakan95@gmail.com"],
        "!!Sicaklik Uyarisi!!", "Sicaklik: %d C" % temperature)
else:
   sendMail(["coskunhakan95@gmail.com"]," ","Sicaklik: %d C" % temperature)


