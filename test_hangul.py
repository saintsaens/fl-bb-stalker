# -*- coding: utf-8 -*-
import hangul


def test_is_hangul():
    assert hangul.is_hangul(u'한글이 줗아') is True
    assert hangul.is_hangul(u'한') is True
    assert hangul.is_hangul(u'hello') is False
