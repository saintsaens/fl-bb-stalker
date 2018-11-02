# -*- coding: utf-8 -*-
def is_hangul_character(char):
    """Check if character is in the Hangul Jamo block. MUST BE IN UNICODE."""

    value = ord(char)
    if 44032 <= value <= 55215:
        return True
    return False


def is_hangul(string):
    """Check if there is a character in the Hangul syllables block. MUST BE IN UNICODE."""

    for i in string:
        if is_hangul_character(i):
            return True
    return False
