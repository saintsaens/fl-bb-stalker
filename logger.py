# -*- coding: utf-8 -*-
import csv


def write_in_log(text, log):
    with open(log, 'ab+') as f:
        writer = csv.writer(f)
        writer.writerow([text])


def is_in_log(text, log):
    with open(log, 'ab+') as f:
        reader = csv.reader(f)
        for row in reader:
            if text in row:
                return True
        return False
