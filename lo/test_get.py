from lo.get import get

def test_get():
    params = {"max_length": 100}
    max_length = get(params, 'max_length', 0)
    assert max_length == 100
    foo_bar = get(params, 'foo_bar', 20)
    assert foo_bar == 20
    new_length = get({}, 'new_length', 100)
    assert new_length == 100
