# helper class 

# Attendence/utils.py
from datetime import datetime   # date and time
import pytz  # asia
from .logger import get_logger

logger = get_logger(__name__)

def current_toronto_date():
    """
    Get today's date in America/Toronto timezone.
    This helps ensure consistent attendance records.
    """
    try:
        EST = pytz.timezone("America/Toronto")
        return datetime.now(EST).strftime("%Y-%m-%d")
    except Exception:
        logger.exception("Failed to compute Toronto date")
        # Fallback to UTC date string
        return datetime.now().strftime("%Y-%m-%d")
