"""Custom logger class for the project."""

import logging
import sys
import os
from datetime import datetime

from colorlog import ColoredFormatter

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


class Logger:
    """Custom logger implementation."""

    _instance = None

    def __new__(cls, name, level="DEBUG"):
        """Checks if an instance of the Logger class exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._name = name
            cls._instance._level = level
            cls._instance._configure_logger()
        return cls._instance

    def _configure_logger(self):
        """Configures the logger."""
        formatter = ColoredFormatter(
            "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        )
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        stdout_handler.setLevel(self._level)
        file_handler = logging.FileHandler(LOG_FILE_PATH)
        file_handler.setFormatter(
            logging.Formatter("%(levelname)s : %(name)s : %(message)s")
        )
        file_handler.setLevel(self._level)
        logger = logging.getLogger(self._name)
        logger.setLevel(self._level)
        logger.addHandler(stdout_handler)
        logger.addHandler(file_handler)

    def info(self, msg, *args, **kwargs):
        """Logs an info message."""
        logging.getLogger(self._name).info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """Logs a debug message."""
        logging.getLogger(self._name).debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """Logs a warning message."""
        logging.getLogger(self._name).warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """Logs an error message."""
        logging.getLogger(self._name).error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """Logs a critical message."""
        logging.getLogger(self._name).critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        """Logs a message at the specified level."""
        logging.getLogger(self._name).log(level, msg, *args, **kwargs)
