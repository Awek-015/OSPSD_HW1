import pytest
from unittest.mock import patch, MagicMock
from src.logger import Logger
from src.notifier import Notifier


class TestLoggerNotifierIntegration:
    @pytest.mark.parametrize("value,threshold,should_notify", [
        (15, 10, True),  # exceed threshold
        (5, 10, False),  # below threshold
        (10, 10, False),  # equal to threshold
    ])
    @patch("pathlib.Path.open", new_callable=MagicMock)
    def test_notification_based_on_calculation(
            self, mocked_file, value, threshold, should_notify
    ):
        """
        test notification based on calculation results
        """
        logger = Logger("notifier_test.log")
        notifier = Notifier(threshold=threshold)

        logger.log_calculation("test_operation", value, 0, value)

        assert notifier.send_alert(value) == should_notify

        handle = mocked_file.return_value.__enter__.return_value
        assert "test_operation" in handle.write.call_args_list[-1][0][0]

    @patch("pathlib.Path.open", new_callable=MagicMock)
    def test_error_notification(self, mocked_file):
        """
        test notification based on error message
        """
        logger = Logger("error_test.log")
        notifier = Notifier(threshold=10)

        error_message = "Critical calculation error"
        logger.log_error(error_message)

        assert notifier.send_alert(float('inf'))

        handle = mocked_file.return_value.__enter__.return_value
        assert "Error:" in handle.write.call_args_list[-1][0][0]
