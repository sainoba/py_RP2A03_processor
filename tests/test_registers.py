import pytest
from rp2a03.registers import Registers


@pytest.fixture
def registers():
    return Registers()


def test_carry_flag(registers: Registers):
    assert registers.carry_flag == 0
    registers.carry_flag = 1
    assert registers.carry_flag == 1


def test_zero_flag(registers: Registers):
    assert registers.zero_flag == 0
    registers.zero_flag = 1
    assert registers.zero_flag == 1


def test_interrupt_disable(registers: Registers):
    assert registers.interrupt_disable == 0
    registers.interrupt_disable = 1
    assert registers.interrupt_disable == 1


def test_decimal_mode(registers: Registers):
    assert registers.decimal_mode == 0
    registers.decimal_mode = 1
    assert registers.decimal_mode == 1


def test_break_command(registers: Registers):
    assert registers.break_command == 0
    registers.break_command = 1
    assert registers.break_command == 1


def test_overflow_flag(registers: Registers):
    assert registers.overflow_flag == 0
    registers.overflow_flag = 1
    assert registers.overflow_flag == 1


def test_negative_flag(registers: Registers):
    assert registers.negative_flag == 0
    registers.negative_flag = 1
    assert registers.negative_flag == 1


def test_flags_dont_affect_others(registers: Registers):
    unset_flags = ["carry_flag", "zero_flag", "interrupt_disable",
                   "decimal_mode", "break_command", "overflow_flag",
                   "negative_flag"]
    set_flags = []
    assert registers.status == 0
    while unset_flags:
        flag = unset_flags.pop()
        setattr(registers, flag, 1)
        set_flags.append(flag)
        for flag in unset_flags:
            assert getattr(registers, flag) == 0, "{} should be unset".format(flag)
        for flag in set_flags:
            assert getattr(registers, flag) == 1, "{} should be set".format(flag)
