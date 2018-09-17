import functools
from typing import Callable

base_cycles = {
    0x69: 2,
    0x65: 3,
    0x75: 4,
    0x6d: 4,
    0x7d: 4,
    0x79: 4,
    0x61: 6,
    0x71: 5,
}


class Processor:
    def __init__(self, registers, memory):
        self.registers = registers
        self.memory = memory

    def step(self):
        # Fetch
        for result in self._fetch():
            yield
        opcode = result
        # Decode
        function_ = self._decode(opcode)
        # Execute
        yield from self._execute(function_)

        yield {"opcode": opcode}

    def _fetch(self) -> (int, int):
        instruction = self.memory[self.registers.program_counter]
        self.registers.program_counter += 1
        yield instruction  # a cycle

    def _decode(self, opcode: int) -> Callable:
        if opcode in {0x69, 0x65, 0x75, 0x6d, 0x7d, 0x79, 0x61, 0x71}:  # Add with carry - adc
            fun = self._opcode_adc
        return functools.partial(fun, opcode)

    def _opcode_adc(self, opcode: int):  # Add with carry
        cycles = base_cycles[opcode]

    def __next__(self):
        while True:
            step = self.step()
            for result in step:
                yield
            print("Executed: {}".format(result["opcode"]))
        raise StopIteration

