import pytest

def test_error_raise():
    with pytest.raises(ZeroDivisionError) as e:
        n=1/0
    #assert  "division by zero" in str(e.value) ,"Exception didnt match"
    assert str(e.value).__contains__("division by zero"), "Exception didnt match"
