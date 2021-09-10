""" execute with 'python -m pytest'
"""

import pytest

from ikea_name_generator import *

@pytest.mark.parametrize("input, expected", 
    [
        ("JORDAN", ['Nådroj', 'Nädroj']), 
        ("Jordan", ['Nådroj', 'Nädroj']), 
        ("jordan", ['Nådroj', 'Nädroj']), 
        ("jordan1", ['1nådroj', '1nädroj']),
        ('a', ['Ä', 'Å']),
        ('A', ['Ä', 'Å']),
        ('e', ['Ë']),
        ('i', ['Ï']),
        ('o', ['Ø', 'Ö']),
        ('u', ['Ü']),
        ('sdk', ['Kds']),
    ]
)
def test_gen_ikea_name(input, expected):
    assert gen_ikea_name(input) in expected
