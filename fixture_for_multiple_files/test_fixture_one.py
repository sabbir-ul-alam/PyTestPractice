import pytest

def test_method_1(commonFixture):
    assert commonFixture[0]==36,"First index comparison failed"
