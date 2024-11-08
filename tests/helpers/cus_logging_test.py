import unittest
from unittest.mock import patch, Mock


class CusLogging(unittest.TestCase):

  @patch('os.path.isfile')
  def test_existent_logger(self, mock_isfile: Mock):
    mock_isfile.return_value = True

    from src.common import logger
    my_logger = logger

    my_logger.info("Hello world")
    self.assertTrue(1, 1)

class CusLoggingT(unittest.TestCase):
  @patch('os.path.isfile')
  def test_empty_logger(self, mock_isfile: Mock):
    mock_isfile.return_value = False

    from src.common import logger
    my_logger = logger

    my_logger.info("Hello world")
    self.assertTrue(1, 1)
