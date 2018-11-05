#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import argparse
import conf
import conf_mail
import logging
import urllib2
import csv
import smtplib

# ================================ LOGGER ==========================================
if __name__ == '__main__':
    levels = ['info', 'debug', 'error', 'warning', 'critical']
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', dest='level', default='info',
                        choices=['info', 'debug', 'error', 'warning', 'critical'])
    args = parser.parse_args()
    logging.basicConfig(filename=conf.JOURNAL, format='%(asctime)s - %(levelname)s - %(message)s',
                        level=getattr(logging, args.level.upper()))


def write_in_log(title, text, link, log):
    with open(log, 'a+') as csvfile:
        fieldnames = ['ID', 'Title', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'ID': text, 'Title': title, 'Link': link})


def is_in_log(text, log):
    with open(log, 'ab+') as f:
        reader = csv.reader(f)
        for row in reader:
            if text in row:
                return True
        return False


# ================================ HTML PARSER ====================================
def stalk():
    logging.debug("Fetching threads from https://en.forums.wordpress.com/forum/support/ ...")
    soup = BeautifulSoup(urllib2.urlopen('https://en.forums.wordpress.com/forum/support/').read(), "lxml")

    # Get all threads in their HTML form.
    for thread in soup.find_all(class_=conf.THREAD_CLASS):

        # Extract the title of the thread.
        title = get_thread_title(thread)
        logging.debug("Thread title: " + title)

        # Check if the title is in Korean (must be turned back to unicode).
        if is_hangul(title.decode('utf-8')):
            logging.debug("New Korean thread found: " + title)

            # Get the link and ID of the thread.
            link = get_thread_link(thread)
            logging.debug("Thread link: " + link)
            thread_id = get_thread_id(thread)
            logging.debug("Thread ID: " + thread_id)

            if is_in_log(thread_id, conf.LOG_FILE):
                logging.debug("Thread already in log.")
            else:
                logging.debug("Adding thread to the log...")
                write_in_log(title, thread_id, link, conf.LOG_FILE)
                logging.debug("Thread added to the log.")
                logging.debug("Sending mail...")
                mail_subject = create_subject(title)
                send_email(conf_mail.SRC_EMAIL, conf_mail.SRC_PW, conf_mail.DST_EMAIL, mail_subject, link)
        else:
            logging.debug("Not a Korean title.")


def get_thread_title(thread):
    html_title = thread.find(class_=conf.TITLE_CLASS)
    return html_title.get_text().encode('utf-8')


def get_thread_link(thread):
    html_title = thread.find(class_=conf.TITLE_CLASS)
    return html_title.get('href').encode('utf-8')


def get_thread_id(thread):
    return thread['id']


def thread_is_korean(thread):
    # Extract the title of the thread.
    title = get_thread_title(thread)
    logging.debug("Thread title: " + title)


# ================================ MAIL ==========================================
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
        print 'Mail sent!'
    except:
        print "Failed."


def create_subject(title):
    subject = "New Korean thread: " + title
    return subject


# ================================ KOREAN RECOGNIZER ==============================
def is_hangul(string):
    """Check if there is a character in the Hangul syllables block. MUST BE IN UNICODE."""

    for i in string:
        if 44032 <= ord(i) <= 55215:
            return True
    return False


# ================================ MAIN ===========================================
stalk()