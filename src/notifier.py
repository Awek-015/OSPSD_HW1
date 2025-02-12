class Notifier:
    def __init__(self, threshold: float) -> None:
        """
        Initialize the Notifier with a threshold value.
        :param threshold: The value beyond which a notification is triggered.
        """
        self.threshold = threshold

    def send_alert(self, result: float) -> bool:
        """
        Send an alert if the result exceeds the threshold.
        :param result: The numerical result to check.
        """
        if result > self.threshold:
            print(f"ALERT: The result {result} exceeds the threshold {self.threshold}!")
            return True
        return False