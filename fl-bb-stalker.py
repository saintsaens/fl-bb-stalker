# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from hangul import is_hangul
import conf

soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')

# Get all threads.
for thread in soup.find_all(class_=conf.THREAD_CLASS):

    # Extract the title of the thread.
    title = thread.find(class_=conf.TITLE_CLASS)

    # Extract the title of the thread and encode it in UTF-8.
    text = title.get_text().encode('utf-8')

    # Get the link and ID of the thread.
    link = title.get('href')
    thread_id = thread['id']

    # Check if the thread title is in Korean (must be turned back to unicode).
    if is_hangul(text.decode('utf-8')):
        print("Thread in Korean found: " + text)
        print("Link: " + link)
        print ("ID: " + thread_id)
