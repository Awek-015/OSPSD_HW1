import datetime
class Logger:
    def __init__(self, filename="default.log"):
        self.filename = filename

    def log(self, message):
        """Record a message with a timestamp to a log file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}\n"
        with open(self.filename, 'a') as file:
            file.write(log_message)

    def log_error(self, error):
        """Specifically log errors."""
        self.log(f"Error: {error}")

    def log_calculation(self, operation, a, b, result):
        """Log a calculation and its result."""
        message = f"{operation}({a}, {b}) = {result}"
        self.log(message)
