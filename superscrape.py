# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from hangul import is_hangul
import conf

soup = BeautifulSoup(open("./fake_html.html"), 'html.parser')

for thread in soup.find_all(class_=conf.CLASS):

    # Extract the title of the thread and encode it in UTF-8.
    text = thread.get_text().encode('utf-8')
    link = thread.get('href')

    # Check if the thread title is in Korean (must be turned back to unicode).
    if is_hangul(text.decode('utf-8')):
        print("Thread in Korean found: " + text)
        print("Link: " + link)
