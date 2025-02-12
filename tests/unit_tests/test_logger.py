import unittest
from unittest.mock import MagicMock, patch

from src.logger import Logger


class TestLogger(unittest.TestCase):
    @patch("pathlib.Path.open", new_callable=MagicMock)
    @patch("datetime.datetime")
    def test_log(self, mock_datetime: MagicMock, mocked_file: MagicMock) -> None:
        # Set the mock to return a fixed datetime
        mock_datetime.now.return_value.strftime.return_value = "2025-02-11 12:00:00"

        logger = Logger("test.log")
        logger.log("Test message")

        # Check that Path.open is called correctly
        mocked_file.assert_called_once_with("a")

        # Check that the file write operation is called correctly
        handle = mocked_file.return_value.__enter__.return_value
        handle.write.assert_called_with("2025-02-11 12:00:00 - Test message\n")

    @patch("src.logger.Logger.log")
    def test_log_error(self, mocked_log: MagicMock) -> None:
        logger = Logger()
        logger.log_error("Sample error")
        mocked_log.assert_called_once_with("Error: Sample error")

    @patch("src.logger.Logger.log")
    def test_log_calculation(self, mock_log: MagicMock) -> None:
        logger = Logger("test.log")
        operation = "add"
        a = 5
        b = 3
        result = 8
        logger.log_calculation(operation, a, b, result)
        expected_message = f"{operation}({a}, {b}) = {result}"
        mock_log.assert_called_with(expected_message)

if __name__ == "__main__":
    unittest.main()
