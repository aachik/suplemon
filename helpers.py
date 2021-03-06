#-*- encoding: utf-8
"""
Various helper constants and functions.
"""

import sys
import time
import traceback

# Logging constants
LOG_WONTFIX = 0
LOG_INFO = 1
LOG_WARNING = 2
LOG_ERROR = 3

def curr_time():
    """Current time in %H:%M"""
    return time.strftime("%H:%M")
    
def curr_time_sec():
    """Current time in %H:%M:%S"""
    return time.strftime("%H:%M:%S")

def starts(s, what):
    """Check if a string begins with given string or any one in given list."""
    if type(what) == type(""):
        what = [what]
    for item in what:
        if s.find(item) == 0:
            return True
    return False

def ends(s, what):
    """Check if a string ends with given string or any one in given list."""
    s = s[::-1]
    if type(what) == type(""):
        what = [what]
    for item in what:
        if s.find(item[::-1]) == 0:
            return True
    return False

def get_error_info():
    """Return info about last error."""
    msg = str(traceback.format_exc()) + "\n" + str(sys.exc_info())
    return msg

def get_string_between(start, stop, s):
    """Search string for a substring between two delimeters. False if not found."""
    i1 = s.find(start)
    if i1 == -1:
        return False
    s = s[i1 + len(start):]
    i2 = s.find(stop)
    if i2 == -1:
        return False
    s = s[:i2]
    return s