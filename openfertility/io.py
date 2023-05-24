import logging

def logger():
    """ Common logger for all modules """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    return logging.getLogger()

log = logger()