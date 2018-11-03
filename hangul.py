#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_hangul(string):
    """Check if there is a character in the Hangul syllables block. MUST BE IN UNICODE."""

    for i in string:
        if 44032 <= ord(i) <= 55215:
            return True
    return False
