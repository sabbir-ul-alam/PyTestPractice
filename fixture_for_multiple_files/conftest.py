import pytest

@pytest.fixture
def commonFixture():
    a=25
    b=35
    c=45
    return [a,b,c]
