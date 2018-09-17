import array
import pytest

from rp2a03.processor_by_instruction import Processor
from rp2a03.registers import Registers


@pytest.fixture
def dummy_memory():
    return array.array("B", (0 for _ in range(0xFFFF)))


def test_create_processor(dummy_memory):
    Processor(Registers(), dummy_memory)
