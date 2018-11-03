#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from hangul import is_hangul
import conf
import logger
import mail
import conf_mail
import logging


def stalk():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')

    # Get all threads in their HTML form.
    logging.debug("Getting all threads from HTML source...")
    for thread in soup.find_all(class_=conf.THREAD_CLASS):

        # Extract the title of the thread.
        title = get_thread_title(thread)
        logging.debug("Thread title: " + title)

        # Get the link and ID of the thread.
        link = get_thread_link(thread)
        logging.debug("Thread link: " + link)
        thread_id = get_thread_id(thread)
        logging.debug("Thread ID: " + thread_id)

        # Check if the thread title is in Korean (must be turned back to unicode).
        if is_hangul(title.decode('utf-8')):
            logging.info("New Korean thread found: " + title)
            if logger.is_in_log(thread_id, conf.LOG_FILE):
                logging.info("Thread already in log.")
            else:
                logging.info("Adding thread to the log...")
                logger.write_in_log(title, thread_id, link, conf.LOG_FILE)
                logging.info("Thread added!")
                logging.info("Sending mail...")
                mail_subject = mail.create_subject(title)
                mail.send_email(conf_mail.SRC_EMAIL, conf_mail.SRC_PW, conf_mail.DST_EMAIL, mail_subject, link)


def get_thread_title(thread):
    html_title = thread.find(class_=conf.TITLE_CLASS)
    return html_title.get_text().encode('utf-8')


def get_thread_link(thread):
    html_title = thread.find(class_=conf.TITLE_CLASS)
    return html_title.get('href').encode('utf-8')


def get_thread_id(thread):
    return thread['id']
