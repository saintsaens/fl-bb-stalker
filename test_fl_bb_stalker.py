#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import conf
import fl_bb_stalker


def test_is_hangul():
    assert fl_bb_stalker.is_hangul(u'한글이 줗아') is True
    assert fl_bb_stalker.is_hangul(u'한') is True
    assert fl_bb_stalker.is_hangul(u'hello') is False

def test_get_thread_title():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')
    thread = soup.find(class_=conf.THREAD_CLASS)
    title = fl_bb_stalker.get_thread_title(thread)
    assert title == "Best Practices & Community Standards"


def test_get_thread_link():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')
    thread = soup.find(class_=conf.THREAD_CLASS)
    link = fl_bb_stalker.get_thread_link(thread)
    assert link == "https://en.forums.wordpress.com/topic/best-practices-community-standards/"


def test_get_thread_id():
    soup = BeautifulSoup(open(conf.HTML_FILE), 'html.parser')
    thread = soup.find(class_=conf.THREAD_CLASS)
    thread_id = fl_bb_stalker.get_thread_id(thread)
    assert thread_id == "bbp-topic-3065850"


# def test_thread_is_korean():
