from unittest.mock import MagicMock, patch

from src.calculator import Calculator
from src.logger import Logger


class TestCalculatorLoggerIntegration:
    @patch("pathlib.Path.open", new_callable=MagicMock)
    @patch("datetime.datetime")
    def test_calculator_operations_logging(
            self,
            mock_datetime: MagicMock,
            mocked_file: MagicMock,
    ) -> None:
        """Test that the calculator operations are logged correctly."""
        # Set the mock to return a fixed datetime to simplify
        mock_datetime.now.return_value.strftime.return_value = "2025-02-11 12:00:00"

        logger = Logger("calc_test.log")

        add_result = Calculator.add(5, 3)
        logger.log_calculation("add", 5, 3, add_result)

        sub_result = Calculator.subtract(213, 37)
        logger.log_calculation("subtract", 213, 37, sub_result)

        mult_result = Calculator.multiply(4, 2)
        logger.log_calculation("multiply", 4, 2, mult_result)

        mocked_file.assert_called_with("a")
        handle = mocked_file.return_value.__enter__.return_value

        # Verify that the log messages are written to the file
        expected_calls = [
            "2025-02-11 12:00:00 - add(5, 3) = 8\n",
            "2025-02-11 12:00:00 - subtract(213, 37) = 176\n",
            "2025-02-11 12:00:00 - multiply(4, 2) = 8\n",
        ]
        assert handle.write.call_count == 3
        handle.write.assert_any_call(expected_calls[0])
        handle.write.assert_any_call(expected_calls[1])
        handle.write.assert_any_call(expected_calls[2])
