import pytest

def test_none():
    assert None is None

def test_skip():
    pytest.skip("Skipped test...")

def test_fail():
    assert 1 / 0