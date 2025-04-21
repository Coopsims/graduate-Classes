import os
import logging


def get_logger():
    """
    Creates and configs logger for tracking application events and errors.

    Returns:
        logging.Logger: pre-con logger instance for writing logs to a file.
    """
    log_dir = os.path.join(os.path.dirname(__file__), "..", "files", "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, "getting_out_of_debt.log")

    logger = logging.getLogger("DebtLogger")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(lineno)d: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
