# -*- coding: utf-8 -*-
import csv


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
