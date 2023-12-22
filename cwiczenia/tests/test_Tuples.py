from test_firstPassingTest import Ziomki


def test_asDictionary():
    ziomek = Ziomki('Krzywy', 'Krzywicki', 35, True)
    dictonaryItem = ziomek._asdict()
    expected = {'imie': 'Krzywy', 'nazwisko': 'Krzywicki', 'wiek': 35, 'czyPije': True}
    assert dictonaryItem == expected

def test_member_access():
    z = Ziomki('Kowal', 'Kowaluk')
    assert z.imie == 'Kowal'
    assert z.nazwisko == 'Kowaluk'
    assert (z.wiek, z.czyPije)

def test_ziomki_equality():
    z1 = Ziomki('Patrycja', 'Mazur')
    z2 = Ziomki('Patrycja', 'Mazur')
    assert z1 == z2
