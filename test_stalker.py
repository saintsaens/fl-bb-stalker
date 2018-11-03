#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import stalker
import conf


def test_get_thread_title():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')
    thread = soup.find(class_=conf.THREAD_CLASS)
    title = stalker.get_thread_title(thread)
    assert title == "Best Practices & Community Standards"


def test_get_thread_link():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')
    thread = soup.find(class_=conf.THREAD_CLASS)
    link = stalker.get_thread_link(thread)
    assert link == "https://en.forums.wordpress.com/topic/best-practices-community-standards/"


def test_get_thread_id():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')
    thread = soup.find(class_=conf.THREAD_CLASS)
    thread_id = stalker.get_thread_id(thread)
    assert thread_id == "bbp-topic-3065850"
