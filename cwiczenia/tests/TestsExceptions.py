import pytest
import tasks
from test_firstPassingTest import Ziomki


def test_type_error():
    with pytest.raises(AttributeError):
        tasks.add(task='not a task object')


# @pytest.mark.jedziemy
def test_raise_value_error():
    with pytest.raises(TypeError) as lipa:
        dodawanie('jas', 4)
    print(lipa)


# @pytest.mark.jedziemy
def test_raise_value_error_message():
    with pytest.raises(TypeError) as lipa:
        dodawanie('jas', 4)
    exception_msg = lipa.value.args[0]
    print(exception_msg)
    # assert exception_msg == "can only con..."int") to str"


# @pytest.mark.jedziemy
def test_unique_id():
    id_1 = Ziomki(nazwisko='SuperZiomek')
    id_2 = Ziomki(nazwisko='SuperZiomek')
    assert id_1 == id_2


def dodawanie(a, b):
    return a + b

try:
    dodawanie('jas', 3)
except:
    TypeError
