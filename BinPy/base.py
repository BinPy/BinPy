from __future__ import print_function
import warnings
import logging

consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
consoleHandler.setFormatter(formatter)
logger = logging.getLogger('Main Logger')
logger.addHandler(consoleHandler)


def init_logging(log_level):
    logger.setLevel(log_level)


def read_logging_level(log_level):
    levels_dict = {
        1: logging.DEBUG, "debug": logging.DEBUG,
        2: logging.INFO, "info": logging.INFO,
        3: logging.WARNING, "warning": logging.WARNING,
        4: logging.ERROR, "error": logging.ERROR,
        5: logging.CRITICAL, "critical": logging.CRITICAL
    }

    if isinstance(log_level, str):
        log_level = log_level.lower()

    if log_level in levels_dict:
        return levels_dict[log_level]
    else:
        print ("The logging level given is not valid")
        return None


def get_logging_level():
    """
    This function prints the current logging level of the main logger.
    """
    levels_dict = {
        10: "DEBUG",
        20: "INFO",
        30: "WARNING",
        40: "ERROR",
        50: "CRITICAL"
    }

    print (
        "The current logging level is:",
        levels_dict[
            logger.getEffectiveLevel()])


def set_logging(log_level, myfilename=None):
    """
    This function sets the threshold for the logging system and, if desired,
    directs the messages to a logfile. Level options:

    'DEBUG' or 1
    'INFO' or 2
    'WARNING' or 3
    'ERROR' or 4
    'CRITICAL' or 5

    If the user is on the interactive shell and wants to log to file, a custom
    excepthook is set. By default, if logging to file is not enabled, the way
    errors are displayed on the interactive shell is not changed.
    """

    if myfilename and ipython_version:
        try:
            if ipython_version.startswith("0.10"):
                __IPYTHON__.set_custom_exc(
                    (Exception,), ipython_exception_handler)
            else:
                ip = get_ipython()
                ip.set_custom_exc((Exception,), ipython_exception_handler)
        except NameError:  # In case the interactive shell is not being used
            sys.exc_clear()

    level = read_logging_level(log_level)

    if level and myfilename:
        fileHandler = logging.FileHandler(filename=myfilename)
        fileHandler.setLevel(level)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.removeHandler(consoleHandler)  # Console logging is disabled.
        print ("Now logging to", myfilename, "with level", log_level)
    elif level:
        print ("Now logging with level", log_level)

    logger.setLevel(level)
