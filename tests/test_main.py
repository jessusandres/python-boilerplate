import traceback
import unittest

from unittest.mock import patch, MagicMock, Mock
from main import main


class JsonifyMock:
  def __init__(self, data):
    self.data = data

  def get_json(self):
    return self.data


class TestMainFunction(unittest.TestCase):

  @patch('main.get_event_types')
  @patch('main.say_welcome')
  @patch('main.logger')
  @patch('functions_framework.http')
  def test_main_success(self, mock_functions_framework: Mock, mock_logger: Mock, mock_say_welcome: Mock,
                        get_event_types: Mock):
    mock_records = []

    mock_say_welcome.return_value = None
    mock_functions_framework.return_value = MagicMock()
    get_event_types.return_value = mock_records

    # Mock jsonify function
    with patch('main.jsonify', JsonifyMock):
      response = main(None)

      # validate if say_welcome is called without params
      mock_say_welcome.assert_called_with("Stranger")

      # validate if say_welcome is called only once
      mock_say_welcome.assert_called_once()
      # assert mock_say_welcome.call_count == 1

      expected_data = {
        "message": "Execution completed successfully",
        "records": mock_records
      }

      # Validate logs
      mock_logger.info.assert_any_call("* * * * * * * * * Starting process * * * * * * * * *")
      mock_logger.info.assert_any_call(
        f"Job completed with value: {expected_data}")

      # Validate the response
      self.assertEqual(response[0].get_json(), expected_data)
      self.assertEqual(response[1], 201)

  @patch('main.say_welcome')
  @patch('main.logger')
  @patch('functions_framework.http')
  def test_main_exception(self, mock_functions_framework: Mock, mock_logger: Mock, mock_say_welcome: Mock):
    error_msg = "Some controlled error"
    exception = Exception(error_msg)
    mock_functions_framework.return_value = MagicMock()

    # Emulate an exception into merge_raw_with_staging
    mock_say_welcome.side_effect = exception

    with patch('main.jsonify', JsonifyMock):
      response = main(None)

      # Validate logs
      mock_logger.error.assert_any_call('DATA_OBS_INV | Main function exception: %s', error_msg)
      mock_logger.error.assert_any_call(traceback.print_exception(type(exception), exception, exception.__traceback__))

      # Validate response
      self.assertEqual(response[0].get_json(), {"code": 500, "error_msg": error_msg})
      self.assertEqual(response[1], 500)


if __name__ == '__main__':
  unittest.main()
