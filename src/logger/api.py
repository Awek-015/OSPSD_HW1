"""API for the Logger component."""

from .logger import Logger


def create_logger(filename: str = "default.log") -> Logger:
    """Create a new logger instance."""
    return Logger(filename)


def log_message(message: str, logger: Logger = None) -> None:
    """Log a message using the specified or default logger."""
    if logger is None:
        logger = create_logger()
    logger.log(message)


def log_error(error: str, logger: Logger = None) -> None:
    """Log an error message using the specified or default logger."""
    if logger is None:
        logger = create_logger()
    logger.log_error(error)


def log_calculation(
    operation: str, a: float, b: float, result: float, logger: Logger = None
) -> None:
    """Log a calculation using the specified or default logger."""
    if logger is None:
        logger = create_logger()
    logger.log_calculation(operation, a, b, result)
