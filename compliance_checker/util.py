"""
General purpose utility functions to aid in compliance checking tasks
"""
import re
import datetime


def isstring(obj):
    try:
        return isinstance(obj, str)
    except NameError:
        return isinstance(obj, str)


def datetime_is_iso(date_str):
    """Attempts to parse a date formatted in ISO 8601 format"""
    passed = datetime_parse(date_str)
    if not passed and '+' in date_str:
        dateparts = date_str.split('+')
        passed = datetime_parse(dateparts[0]) and re.match(r"\d\d:\d\d", dateparts[1])
    if passed:
        return True, []
    else:
        return False, ['Datetime provided is not in a valid ISO 8601 format']

def datetime_parse(datetime_string):
    """Brute force datetime validation"""
    for date_template in [
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
        "%Y%m%d",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y%m%dT%H%M%SZ",
        "%Y-W%W",
        "%Y-W%W-%w",
        "%Y-%j",
    ]:
        try:
            dt = datetime.datetime.strptime(datetime_string, date_template)
            return True
        except:  # Any error qualifies as not ISO format
            pass
    return False

def dateparse(date_str):
    '''
    Returns a naive datetime. parsed from an ISO-8601 input string

    :param str date_str: An ISO-8601 string
    '''

    return datetime.datetime(*list(map(int, re.split('[^\d]', date_str)[:-1])))

