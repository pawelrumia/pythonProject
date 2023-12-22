import pytest


def func(x):
    return x + 1

def raise_exception():
    raise SystemExit(1)

def test_answer():
    assert func(3) == 4

def test_system_exit():
    assert pytest.raises(SystemExit)
