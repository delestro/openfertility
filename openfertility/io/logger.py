import logging


def set_detailed_output():
    formatter = logging.Formatter(
        "%(levelname)-10s%(filename)s:%(lineno)-5s%(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger("openfertility")
    logger.handlers = []
    logger.addHandler(handler)


def set_simple_output():
    formatter = logging.Formatter("%(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger("openfertility")
    logger.handlers = []
    logger.addHandler(handler)


def set_level_DEBUG():
    logging.getLogger("openfertility").setLevel(logging.DEBUG)


def set_level_INFO():
    logging.getLogger("openfertility").setLevel(logging.INFO)


def set_level_WARNING():
    logging.getLogger("openfertility").setLevel(logging.WARNING)


def set_level_ERROR():
    logging.getLogger("openfertility").setLevel(logging.ERROR)


def set_level_CRITICAL():
    logging.getLogger("openfertility").setLevel(logging.CRITICAL)


def level(level):
    """Set the logging level based on the specified level.

    Args:
        level (str or int): The logging level to set. It can be one of the following:
            - "DEBUG" or "debug": Set the logging level to DEBUG.
            - "INFO" or "info": Set the logging level to INFO.
            - "WARNING" or "warning": Set the logging level to WARNING.
            - "ERROR" or "error": Set the logging level to ERROR.
            - "CRITICAL" or "critical": Set the logging level to CRITICAL.
            - int: Set the logging level using the numeric value of the level (e.g., logging.DEBUG).

    Raises:
        ValueError: If the specified level is not a valid logging level.

    """
    if level in ["DEBUG", "debug"]:
        set_level_DEBUG()

    elif level in ["INFO", "info"]:
        set_level_INFO()

    elif level in ["WARNING", "warning"]:
        set_level_WARNING()

    elif level in ["ERROR", "error"]:
        set_level_ERROR()

    elif level in ["CRITICAL", "critical"]:
        set_level_CRITICAL()

    elif isinstance(level, int):
        logging.getLogger("openfertility").setLevel(level)

    else:
        raise ValueError(
            f"Invalid logging level: '{level}'.\nPlease use 'debug', 'info', 'warning', 'error', 'critical' or an int."
        )


# create the logger
log = logging.getLogger("openfertility")
set_simple_output()
set_level_INFO()
