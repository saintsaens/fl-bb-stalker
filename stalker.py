#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from hangul import is_hangul
import conf
import logger
import mail
import conf_mail
import logging
import urllib2


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

            if logger.is_in_log(thread_id, conf.LOG_FILE):
                logging.debug("Thread already in log.")
            else:
                logging.debug("Adding thread to the log...")
                logger.write_in_log(title, thread_id, link, conf.LOG_FILE)
                logging.debug("Thread added to the log.")
                logging.debug("Sending mail...")
                mail_subject = mail.create_subject(title)
                mail.send_email(conf_mail.SRC_EMAIL, conf_mail.SRC_PW, conf_mail.DST_EMAIL, mail_subject, link)
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
