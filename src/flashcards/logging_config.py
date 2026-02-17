import logging
import logging.config
import os

from pythonjsonlogger import json


def get_standard_formatter() -> logging.Formatter:
    """Structured JSON formatter for production logs."""
    return json.JsonFormatter("%(asctime)s %(name)s %(levelname)s %(message)s %(module)s %(funcName)s %(lineno)d")


def configure_logging() -> None:
    """Configure loggers, handlers, and formatters."""
    level = os.getenv("LOG_LEVEL", "INFO").upper()

    handlers = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": level,
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "level": level,
            "filename": "app.log",
            "maxBytes": 10_485_760,
            "backupCount": 5,
            "encoding": "utf-8",
        },
    }

    formatters = {
        "json": {"()": json.JsonFormatter, "format": "%(asctime)s %(name)s %(levelname)s %(message)s %(module)s"}
    }

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": formatters,
            "handlers": handlers,
            "root": {
                "handlers": ["console", "file"],
                "level": level,
            },
            "loggers": {
                "uvicorn": {"level": "WARNING", "handlers": ["console"], "propagate": False},
                "sqlalchemy": {"level": "WARNING", "handlers": ["console"], "propagate": False},
            },
        }
    )
