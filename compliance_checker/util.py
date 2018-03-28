"""
General purpose utility functions to aid in compliance checking tasks
"""
import re
import datetime


def isstring(obj):
    try:
        return isinstance(obj, basestring)
    except NameError:
        return isinstance(obj, str)


def datetime_is_iso(date_str):
    """Attempts to parse a date formatted in ISO 8601 format"""
    try:
        if len(date_str) > 20:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.Z")
        elif len(date_str) > 10:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        else:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True, []
    except:  # Any error qualifies as not ISO format
        return False, ['Datetime provided is not in a valid ISO 8601 format']


def dateparse(date_str):
    '''
    Returns a naive datetime. parsed from an ISO-8601 input string

    :param str date_str: An ISO-8601 string
    '''

    return datetime.datetime(*map(int, re.split('[^\d]', s)[:-1]))

