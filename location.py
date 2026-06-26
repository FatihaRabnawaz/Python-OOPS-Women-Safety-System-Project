# location.py
# Simulates location data using latitude and longitude.

class Location:
    """
    Represents a geographical location. For simulation, we use a fixed location.
    In a real app, this could fetch from GPS hardware.
    """

    def __init__(self, latitude=28.6139, longitude=77.2090):
        """
        Default location: New Delhi, India (can be changed).
        """
        self.__latitude = latitude    # Private attributes
        self.__longitude = longitude

    def get_location(self):
        """
        Returns a tuple (latitude, longitude).
        """
        return (self.__latitude, self.__longitude)

    def display_location(self):
        """Return a formatted string of the current location."""
        lat, lon = self.get_location()
        return f"Latitude: {lat}, Longitude: {lon}"