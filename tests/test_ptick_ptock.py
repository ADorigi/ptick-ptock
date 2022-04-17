import pytest
import datetime

from src.ptick_ptock import ptick_ptock

ptick_ptock_object = None

@pytest.fixture(scope="function")
def ptick_ptock_object():
    ptick_ptock_object = ptick_ptock()
    yield ptick_ptock_object

def test_before_ptick(ptick_ptock_object):
    assert ptick_ptock_object.isTicked() == True

def test_ptick(ptick_ptock_object):
    ptick_ptock_object.ptick()
    assert ptick_ptock_object.isTicked() == False

def test_datetime_ptock(ptick_ptock_object):
    ptick_ptock_object.ptick()
    assert isinstance(ptick_ptock_object.datetime_ptock(),datetime.timedelta)

def test_print_ptock(ptick_ptock_object):
    ptick_ptock_object.ptick()
    try:
        ptick_ptock_object.print_ptock()
    except Exception:
        assert False
    
    assert True
