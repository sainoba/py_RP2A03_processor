class Processor:
    def __init__(self, registers, memory):
        self.registers = registers
        self.memory = memory

    def tick(self) -> dict:
        opcode = self._fetch()
        _function = self._decode(opcode)
        cycles = self._execute(_function)
        return {"cycles": cycles, "opcode": opcode}

    def _fetch(self) -> int:
        instruction = self.memory[self.registers.program_counter]
        self.registers.program_counter += 1
        return instruction

    def _decode(self, opcode: int) -> function:
        return lambda: None
