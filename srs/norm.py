# -*- coding: utf-8 -*-
"""Normalization and cleanup."""
import re

from unidecode import unidecode

TM_SYMBOLS = u'®\u2120™'  # 2120 is SM symbol

# matches all whitespace, including non-ascii (e.g. non-breaking space)
WHITESPACE_RE = re.compile(r'\s+', re.U)


def clean_string(s):
    """Convert to unicode, remove extra whitespace, and
    convert fancy apostrophes."""
    s = unicode(s)
    s = WHITESPACE_RE.sub(' ', s).strip()
    s = s.replace(u'\u2019', "'")  # "smart" apostrophe
    return s


def merge(src, dst):
    """Merge src dictionary into dst. Only overwrite blank values."""
    for k, v in src.iteritems():
        if v is not None and (v != '' or not dst.get(k)):
            dst[k] = v


def smunch(s):
    """Normalize s and remove whitespace. Useful for, say
    matching brand names against things in alt tags."""
    return WHITESPACE_RE.sub('', unidecode(s).lower())
