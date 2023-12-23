import logging
from colorama import Fore, Style

Fore.BLUE, Fore.YELLOW, Fore.RED, Style.RESET_ALL

log_colors = {
    'DEBUG': Fore.YELLOW,
    'INFO': Fore.BLUE,
    'WARNING': Fore.YELLOW,
    'ERROR': Fore.RED,
    'CRITICAL': Fore.RED
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        message = record.msg
        prefix = f"[{levelname}]"
        color = log_colors.get(levelname, Fore.WHITE)
        return f"{color}{prefix}{Style.RESET_ALL} - {message}"

def setup_colored_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    formatter = ColorFormatter()
    handler.setFormatter(formatter)

    logger.handlers = []

    logger.addHandler(handler)
    return logger

colored_logger = setup_colored_logger()
