import pytest

from round1 import compare_strings

test_cases = [
    {
        "string1": "CODEBANC",
        "string2": "ABC",
        "expected": "BANC",
    },
    {
        "string1": "abc",
        "string2": "def",
        "expected": "",
    },
    {
        "string1": "abc",
        "string2": "abc",
        "expected": "abc",
    },
    {
        "string1": "ABC",
        "string2": "abc",
        "expected": "",
    },
    {
        "string1": "balloonnoollab",
        "string2": "balloon",
        "expected": "balloon",
    },
    {
        "string1": "something",
        "string2": "somethings",
        "expected": "",
    },
    {
        "string1": "aaaoutaaa",
        "string2": "tou",
        "expected": "out",
    },
    {
        "string1": "somesthing",
        "string2": "something",
        "expected": "omesthing",
    }
]

def test_strings():
    for tc in test_cases:
        output = compare_strings(tc["string1"], tc["string2"])
        assert output == tc["expected"]
