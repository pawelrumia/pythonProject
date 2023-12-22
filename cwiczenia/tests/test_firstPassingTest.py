from collections import namedtuple




def test_Passing():
    assert (1, 2, 3) == (1, 2, 3)


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Ziomki = namedtuple('Ziomki', ['imie', 'nazwisko', 'wiek', 'czyPije'])

Task.__new__.__defaults__ = (None, None, False, None)
Ziomki.__new__.__defaults__ = (None, None, None, False)


def test_Defaults():
    """using no parameters"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    people = Task('Jasiulenka', 'Patryszka')
    assert people.summary == 'Jasiulenka'
    assert people.owner == 'Patryszka'
    assert (people.done, people.id) == (False, None)


def test_ziomki_basic():
    ziomki = Ziomki('Krakers', 'Dragun', 38, True)
    assert ziomki.imie == 'Krakers'
    assert Ziomki(None, None, None, False) == Ziomki()
    assert ziomki == Ziomki('Krakers', 'Dragun', 38, True)

# @pytest.mark.cooltest
def test_asdict():
    ziomek1 = Ziomki('Kowal', 'Kowaluk', 39, True)
    ziomek_dict = ziomek1._asdict()
    expected = {'imie': 'Kowal', 'nazwisko': 'Kowaluk', 'wiek': 39, 'czyPije': True}
    assert ziomek_dict == expected


def test_replace():
    ziomek_before = Ziomki('Gangster', 'Szalej', 20, False)
    ziomek_after = ziomek_before._replace(wiek=21, czyPije=True)
    expected = Ziomki('Gangster', 'Szalej', 21, True)
    assert ziomek_after == expected
