# alarm.py
# Simulates an alarm/siren.

class Alarm:
    """
    Represents an alarm/siren system. Currently prints a message.
    """

    def __init__(self):
        self.is_active = False

    def activate(self):
        """Trigger the alarm."""
        self.is_active = True
        # In a real app, you would play a sound or send a signal.
        return "🚨 ALARM! SIREN ACTIVATED! 🚨"

    def deactivate(self):
        """Deactivate the alarm."""
        self.is_active = False
        return "Alarm deactivated."

    def status(self):
        """Return current alarm status."""
        return "Active" if self.is_active else "Inactive"