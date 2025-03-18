import logging
import colorlog

# Create a custom formatter with colors
log_format = "%(log_color)s%(asctime)s - %(levelname)s - %(message)s"
formatter = colorlog.ColoredFormatter(
    log_format,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }
)

# Set up logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create console handler and set formatter
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)