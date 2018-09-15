from ctypes import c_int8, c_uint8, c_uint16


class Registers:
    def __init__(self):
        self.program_counter = 0
        self.stack_pointer = 0
        self.status = 0
        self.accumulator = 0
        self.x = 0
        self.y = 0

    def __setattr__(self, name, value):
        if name in ["x", "y", "accumulator"]:
            value = c_int8(value).value
        elif name in ["status", "stack_pointer"]:
            value = c_uint8(value).value
        elif name is "program_counter":
            value = c_uint16(value).value
        super().__setattr__(name, value)

    @staticmethod
    def _get_flag(flag: int, position: int) -> int:
        return flag >> position & 1

    @staticmethod
    def _set_flag(flag: int, position: int, value: int) -> int:
        flag &= ~(1 << position)
        return flag | (value << position)

    @property
    def carry_flag(self) -> int:
        return self._get_flag(self.status, 0)

    @carry_flag.setter
    def carry_flag(self, value: int):
        self.status = self._set_flag(self.status, 0, value)

    @property
    def zero_flag(self) -> int:
        return self._get_flag(self.status, 1)

    @zero_flag.setter
    def zero_flag(self, value: int):
        self.status = self._set_flag(self.status, 1, value)

    @property
    def interrupt_disable(self) -> int:
        return self._get_flag(self.status, 2)

    @interrupt_disable.setter
    def interrupt_disable(self, value: int):
        self.status = self._set_flag(self.status, 2, value)

    @property
    def decimal_mode(self) -> int:
        return self._get_flag(self.status, 3)

    @decimal_mode.setter
    def decimal_mode(self, value: int):
        self.status = self._set_flag(self.status, 3, value)

    @property
    def break_command(self) -> int:
        return self._get_flag(self.status, 4)

    @break_command.setter
    def break_command(self, value: int):
        self.status = self._set_flag(self.status, 4, value)

    @property
    def overflow_flag(self) -> int:
        return self._get_flag(self.status, 6)

    @overflow_flag.setter
    def overflow_flag(self, value: int):
        self.status = self._set_flag(self.status, 6, value)

    @property
    def negative_flag(self) -> int:
        return self._get_flag(self.status, 7)

    @negative_flag.setter
    def negative_flag(self, value: int):
        self.status = self._set_flag(self.status, 7, value)
