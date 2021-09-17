import  pytest
from TestAutomationUniversity.Stuff.acuum import Accumulator
def test_accumulator_init():
  object = Accumulator()
  assert object.count == 0


def test_accumulator_add_one(object):
  object.add()
  assert object.count == 1


def test_accumulator_add_three(object):

  object.add(3)
  assert object.count == 3


def test_accumulator_add_twice(object):

  object.add()
  object.add()
  assert object.count == 2


def test_accumulator_cannot_set_count_directly(object):

  with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    object.count = 10