# my_utilities/logger.py
import logging
import os

def custom_logger(log_level=logging.DEBUG):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(log_level)

    # File handler
    os.makedirs("logs", exist_ok=True)
    fh = logging.FileHandler("logs/test_log.log", mode='w')
    fh.setFormatter(formatter)
    fh.setLevel(log_level)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger

# 👇 ADD THIS LINE TO FIX THE ISSUE
log = custom_logger()

# import logging
#
# log = logging.getLogger(__name__)
# log.setLevel(logging.INFO)
#
# handler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# log.addHandler(handler)
