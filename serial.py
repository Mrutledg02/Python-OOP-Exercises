"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize the SerialGenerator with a starting value"""
        self.start = start
        self.current = start

    def generate(self):
        """Generate the next serial number."""
        serial_number = self.current
        self.current += 1
        return serial_number
    
    def reset(self):
        """Reset the serial number to the starting value."""
        self.current = self.start

    def __repr__(self):
        """Return a string representation of the SerialGenertor instance."""
        return f"<SerialGenerator start={self.start} next={self.current}"
        