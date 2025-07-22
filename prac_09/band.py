class Band:
    """Represents a band."""
    def __init__(self, name=""):
        """Initialize the band."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)
