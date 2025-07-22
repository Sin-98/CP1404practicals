class Band:
    """Represents a band."""
    def __init__(self, name=""):
        """Initialize the band."""
        self.name = name
        self.members = []



    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Return a string of each member playing."""
        return "\n".join(member.play() for member in self.members)