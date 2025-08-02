class Band:
    """Represents a band."""
    def __init__(self, name=""):
        """Initialize the band."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the band."""
        members_str = ", ".join(str(member) for member in self.members)
        return f"{self.name} ({members_str})"

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Return a string of each member playing."""
        return "\n".join(member.play() for member in self.members)