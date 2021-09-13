import pytest

@pytest.fixture
def fixture_a():
    return  "Oishi"


@pytest.fixture
def fixture_b(fixture_a):
    return  "Ishmam Shamsi"+fixture_a

def test_fullname(fixture_b):
    name="Ishmam Shamsi oishi"
    assert name==fixture_b,"Name didnt match"

