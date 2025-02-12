
from src.notifier import Notifier  # Import without 'src' in the path

import unittest

class TestNotifier(unittest.TestCase):
    def test_notification_triggered(self):
        notifier = Notifier(threshold=100)
        self.assertTrue(notifier.send_alert(150))  # Exceeds threshold

    def test_no_notification(self):
        notifier = Notifier(threshold=100)
        self.assertFalse(notifier.send_alert(50))  # Below threshold

if __name__ == "__main__":
    unittest.main()
