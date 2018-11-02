# -*- coding: utf-8 -*-
import re
import conf


def write_in_log(text):
    # Open a file in write mode
    log_file = open(conf.HTML_FILE, "a+")
    log_file.write(text)
    log_file.close()


def is_in_log(text, log):
    # If file doesn't exist, create it.
    with open(log, "a+") as f:
        for line in f:
            if re.search(text, line):
                return True
        return False
