# program/custom_logger.py
import logging
import os

def my_logger(log_path):
    # Ensure the folder exists
    os.makedirs(log_path, exist_ok=True)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(log_path, "my_log.log")
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    # Example formatter: timestamp::line_number::message
    formatter = logging.Formatter("%(asctime)s::%(lineno)d::%(message)s")
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    # Sample debug message
    logger.debug("Working")

    return logger