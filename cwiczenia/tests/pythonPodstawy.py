def test_printTypes():
    a = 1
    b = 2.8
    c = 2 + 2j
    assert type(a) == int
    assert type(b) == float
    assert type(c) == complex

def test_substringContent():
    stringExample = 'Patiszon'
    result = stringExample[4:]
    assert result == 'szon'

