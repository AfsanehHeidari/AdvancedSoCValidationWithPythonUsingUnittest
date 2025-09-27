# soc.py
class SoC:
    """Simple SoC model with registers and reset (TRST)."""

    def __init__(self):
        # Default register values
        self.default_registers = {
            0x00: 0x00,
            0x04: 0x11,
            0x08: 0x22,
            0x0C: 0x33
        }
        self.registers = dict(self.default_registers)

    def reset(self):
        """Simulate TRST (test reset) by restoring default values."""
        self.registers = dict(self.default_registers)

    def read_register(self, addr):
        """Read a register value."""
        return self.registers.get(addr, None)

    def write_register(self, addr, value):
        """Write to a register if the address is valid."""
        if addr in self.registers:
            self.registers[addr] = value
            return True
        return False
