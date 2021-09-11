import pytest


@pytest.fixture
def fixtureFuction():
    a=25
    b=35
    c=45
    return  [a,b,c]


def test_func_one(fixtureFuction):
    assert fixtureFuction[0]==35," Comparison failed"
def test_func_two(fixtureFuction):
    assert fixtureFuction[1]==35," 2nd placed matched"





