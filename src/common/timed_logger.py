import time

from functools import wraps
from src.common.cus_logging import logger


def timed(func):
  """This decorator prints the execution time for the decorated function."""

  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    logger.info("DATA_OBS_INV | Function >> {} << has taken {} seconds".format(func.__name__, round(end - start, 2)))

    return result

  return wrapper