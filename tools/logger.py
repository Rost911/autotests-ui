import logging


def get_logger(name: str) -> logging.Logger:
    # Initialize a logger with the specified name
    logger = logging.getLogger(name)

    # Set the logger level to DEBUG
    # so it processes all messages with level DEBUG and above
    logger.setLevel(logging.DEBUG)

    # Create a handler that outputs logs to the console
    handler = logging.StreamHandler()

    # Set the handler level to DEBUG
    # so it processes all messages with level DEBUG and above
    handler.setLevel(logging.DEBUG)

    # Configure the log message format:
    # timestamp, logger name, log level, and message
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )
    handler.setFormatter(formatter)  # Apply the formatter to the handler

    # Add the handler to the logger
    logger.addHandler(handler)

    # Return the configured logger
    return logger