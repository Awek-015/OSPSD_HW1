import unittest
from src.notifier import Notifier

class TestNotifier(unittest.TestCase):
    def test_notification_triggered(self):
        notifier = Notifier(threshold=100)
        assert notifier.send_alert(150)  # Exceeds threshold (using regular assert)

    def test_no_notification(self):
        notifier = Notifier(threshold=100)
        assert not notifier.send_alert(50)  # Exceeds threshold (using regular assert)

if __name__ == "__main__":
    unittest.main()