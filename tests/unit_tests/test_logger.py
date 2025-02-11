import unittest
from src.logger import Logger
from unittest.mock import patch, mock_open
class TestLogger(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('datetime.datetime')
    def test_log(self, mock_datetime, mocked_file):
        # Set the time for the mock to return
        mock_datetime.now.return_value.strftime.return_value = "2025-02-11 12:00:00"

        logger = Logger("test.log")
        logger.log("Test message")

        # Check whether the log file is called
        mocked_file.assert_called_once_with("test.log", "a")

        # Check whether the log is written correctly, using the simulated time
        mocked_file().write.assert_called_with("2025-02-11 12:00:00 - Test message\n")

    @patch.object(Logger, 'log')
    def test_log_error(self, mocked_log):
        logger = Logger()
        logger.log_error("Sample error")
        mocked_log.assert_called_once_with("Error: Sample error")

    @patch.object(Logger, 'log')
    def test_log_calculation(self, mock_log):
        logger = Logger("test.log")

        # Test data
        operation = "add"
        a = 5
        b = 3
        result = 8  # The expected result of 5+3

        logger.log_calculation(operation, a, b, result)

        # Build the expected log message
        expected_message = f"{operation}({a}, {b}) = {result}"

        # Verify that the log method is called correctly
        mock_log.assert_called_with(expected_message)


if __name__ == '__main__':
    unittest.main()
