import unittest
from src.memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_write_and_read(self):
        address = 0x00FF
        value = 0xAB
        self.memory.write(address, value)
        self.assertEqual(self.memory.read(address), value)

    def test_read_uninitialized_memory(self):
        address = 0x0000
        self.assertEqual(self.memory.read(address), 0)

    def test_write_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.memory.write(0xFFFF, 0x01)

    def test_read_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.memory.read(0xFFFF)

if __name__ == '__main__':
    unittest.main()