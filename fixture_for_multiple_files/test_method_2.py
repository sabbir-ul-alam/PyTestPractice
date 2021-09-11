import pytest

def test_method_2(commonFixture):
    assert commonFixture[1]==35," second comparison failed"