class Notifier:
    def __init__(self, threshold: float) -> None:

        self.threshold = threshold

    def send_alert(self, result: float) -> bool:

        if result > self.threshold:
            print(f"ALERT: The result {result} exceeds the threshold {self.threshold}!")
            return True
        return False
