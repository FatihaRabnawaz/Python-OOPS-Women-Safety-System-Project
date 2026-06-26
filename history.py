# history.py
# Manages incident history for a user. Records timestamp and description.

import os
from datetime import datetime

class History:
    """
    Logs incidents with timestamp and description.
    Each user has a separate history file.
    """

    def __init__(self, username):
        self.username = username
        self.filename = f"data/{username}_history.txt"
        self.entries = []  # List of (timestamp, description) tuples
        self.load_history()

    def add_entry(self, description):
        """
        Add a new incident entry with current timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = (timestamp, description)
        self.entries.append(entry)
        self.save_history()
        return entry

    def get_history(self):
        """Return a list of all entries as strings."""
        if not self.entries:
            return ["No history records."]
        return [f"{ts} - {desc}" for ts, desc in self.entries]

    def save_history(self):
        """Save all entries to the user's history file."""
        os.makedirs("data", exist_ok=True)
        with open(self.filename, "w") as f:
            for ts, desc in self.entries:
                f.write(f"{ts}|{desc}\n")

    def load_history(self):
        """Load history from file."""
        self.entries = []
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split("|", 1)
                    if len(parts) == 2:
                        timestamp, description = parts
                        self.entries.append((timestamp, description))
        except IOError as e:
            print(f"Error loading history: {e}")