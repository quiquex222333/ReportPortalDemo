import pytest
from demo.my_logger import my_logger

def test_sum():
    """
    My first test
    """
    my_logger.info("todo lo que queramos")
    my_logger.warning("todo lo que queramos 2")
    assert 1+1 == 2

def test_sum_2():
    my_logger.error("todo lo que queramos 3")
    assert 2 == 2, "la suma es diferente a 2"

def test_sum_3():
    """
    My first test
    """
    assert 1+1 == 2

def suma():
    return 2+2