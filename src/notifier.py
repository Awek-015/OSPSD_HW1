class Notifier:
    def __init__(self, threshold: float) -> None:
        """
        Initializes the Notifier with a threshold value.

        :param threshold: The value beyond which a notification is triggered.
        """
        self.threshold = threshold

    def send_alert(self, result: float) -> bool:
        """
        Sends an alert if the result exceeds the threshold.

        :param result: The numerical result to check.
        """
        if result > self.threshold:
            print(f"ALERT: The result {result} exceeds the threshold {self.threshold}!")
            return True
        return False
