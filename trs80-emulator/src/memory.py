class Memory:
    def __init__(self):
        self.memory = [0] * 65536  # TRS-80 has 64KB of memory

    def read(self, address):
        """Read a byte from memory."""
        if 0 <= address < len(self.memory):
            return self.memory[address]
        raise ValueError("Address out of range")

    def write(self, address, value):
        """Write a byte to memory."""
        if 0 <= address < len(self.memory):
            self.memory[address] = value & 0xFF  # Ensure value is a byte
        else:
            raise ValueError("Address out of range")