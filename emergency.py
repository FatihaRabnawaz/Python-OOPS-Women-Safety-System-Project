# emergency.py
# Represents an emergency contact with name, phone number, and relationship.

class EmergencyContact:
    """
    A contact to be alerted in case of emergency.
    Attributes: name, phone, relationship.
    """

    def __init__(self, name, phone, relationship):
        self.name = name
        self.phone = phone
        self.relationship = relationship

    def __str__(self):
        """String representation for displaying contact details."""
        return f"{self.name} ({self.relationship}) - Phone: {self.phone}"