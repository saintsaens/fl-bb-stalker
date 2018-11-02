#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib


def send_email(src_email, pwd, recipient, subject, body):
    dst_email = recipient if isinstance(recipient, list) else [recipient]

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (src_email, ", ".join(dst_email), subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(src_email, pwd)
        server.sendmail(src_email, dst_email, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


def create_subject(title):
    subject = "New Korean thread: " + title
    return subject
