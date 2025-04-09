import pytest 
from fatorial import fatorial

@pytest.mark.parametrize("factor, expected", [(4, 24),(7, 5040),(5, 120),(6, 720)])

def test_fatorial(factor, expected):
    assert fatorial(factor) == expected