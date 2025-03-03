"""Unit tests for Notifier component."""

import unittest
from unittest.mock import patch, call
import io
import sys

from src.notifier.api import notify, create_notifier


class TestNotifier(unittest.TestCase):
    """Test cases for Notifier component."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_notify(self, mock_stdout):
        """Test notification functionality."""
        notify("Test notification")
        self.assertEqual(mock_stdout.getvalue(), "NOTIFICATION: Test notification\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_notify_with_custom_notifier(self, mock_stdout):
        """Test notification with custom notifier instance."""
        notifier = create_notifier()
        notify("Custom notification", notifier)
        self.assertEqual(mock_stdout.getvalue(), "NOTIFICATION: Custom notification\n")
