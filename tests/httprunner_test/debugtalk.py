import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def username():
    return "admin"

def password():
    return "a123"


def sleep(n_secs):
    time.sleep(n_secs)
