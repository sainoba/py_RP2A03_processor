import pytest
from rp2a03.processor import Processor


@pytest.fixture
def processor():
    return Processor()
