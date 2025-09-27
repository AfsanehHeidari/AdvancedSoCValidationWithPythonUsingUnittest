# test_soc.py
import unittest
from soc import SoC

class TestSoC(unittest.TestCase):
    def setUp(self):
        """Fresh SoC instance before each test."""
        self.soc = SoC()

    def test_register_write_and_read(self):
        """Check if write followed by read returns the same value."""
        self.soc.write_register(0x00, 0xAB)
        self.assertEqual(self.soc.read_register(0x00), 0xAB)

    def test_invalid_address(self):
        """Check invalid reads/writes."""
        self.assertIsNone(self.soc.read_register(0x100))
        self.assertFalse(self.soc.write_register(0x200, 0x55))

    def test_reset_restores_defaults(self):
        """Check reset restores default register values."""
        self.soc.write_register(0x04, 0x77)
        self.soc.write_register(0x08, 0x88)
        self.soc.reset()
        self.assertEqual(self.soc.read_register(0x04), 0x11)
        self.assertEqual(self.soc.read_register(0x08), 0x22)

    def test_multiple_writes(self):
        """Check multiple registers."""
        values = {0x00: 0xAA, 0x04: 0xBB, 0x08: 0xCC}
        for addr, val in values.items():
            self.soc.write_register(addr, val)
        for addr, val in values.items():
            self.assertEqual(self.soc.read_register(addr), val)

if __name__ == "__main__":
    print("Running SoC unittest suite...\n")
    unittest.main(verbosity=2)
