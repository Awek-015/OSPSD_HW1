"""API for the Notifier component."""

from .notifier import Notifier


def create_notifier(threshold: int = 0) -> Notifier:
    """
    Create a new notifier instance.

    Args:
        threshold: The threshold value for notifications

    Returns:
        A new Notifier instance
    """
    return Notifier(threshold=threshold)


def notify(message: str, notifier: Notifier = None) -> None:
    """Send a notification using the specified or default notifier."""
    if notifier is None:
        notifier = create_notifier()
    notifier.notify(message)
