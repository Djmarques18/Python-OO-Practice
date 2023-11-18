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
        self.starting_value = start
        self.a = start

    def generate(self):
        """
        Calling this function will add your 'start' number by 1
        """
        self.a += 1   
        return self.a
    
    def reset(self):
        """
        Calling this function will reset your number back to its start
        """
        self.a = self.starting_value
        return self.starting_value
