"""Module for setting up a custom logger with console and file handlers."""

import logging

# Define log level constants for easy access
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


def setup_logger(name: str, log_level: int = DEBUG) -> logging.Logger:
    """
    Create and configure a logger with console and file handlers.

    :param name: Name of the logger.
    :param log_level: Logging level, default is DEBUG. Use DEBUG, INFO, WARNING, ERROR,
                      or CRITICAL from this module to set the desired log level.
    :return: Configured Logger object.

    Usage:
        from src.custom_logger import setup_logger, INFO
        logger = setup_logger('example_module', log_level=INFO)
        logger.info('This is an info message.')
    """

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Check if handlers are already set up to avoid duplicates
    if not logger.handlers:
        # Create handlers (console and file)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("app.log")

        # Set level for handlers
        console_handler.setLevel(log_level)
        file_handler.setLevel(log_level)

        # Create a formatter and set it for handlers
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
