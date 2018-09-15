import pytest
from rp2a03.rp2a03 import Registers


@pytest.fixture
def register():
    return Registers()


def test_carry_flag(register: Registers):
    assert register.carry_flag == 0
    register.carry_flag = 1
    assert register.carry_flag == 1


def test_zero_flag(register):
    assert register.zero_flag == 0
    register.zero_flag = 1
    assert register.zero_flag == 1


def test_interrupt_disable(register):
    assert register.interrupt_disable == 0
    register.interrupt_disable = 1
    assert register.interrupt_disable == 1


def test_decimal_mode(register):
    assert register.decimal_mode == 0
    register.decimal_mode = 1
    assert register.decimal_mode == 1


def test_break_command(register):
    assert register.break_command == 0
    register.break_command = 1
    assert register.break_command == 1


def test_overflow_flag(register):
    assert register.overflow_flag == 0
    register.overflow_flag = 1
    assert register.overflow_flag == 1


def test_negative_flag(register):
    assert register.negative_flag == 0
    register.negative_flag = 1
    assert register.negative_flag == 1
