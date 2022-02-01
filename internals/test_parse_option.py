# from types import SimpleNamespace
from internals.parse_option import parse_option

def test_parse_option():
    option = {"max_length": 100}
    max_length = parse_option(option, 'max_length', 0)
    assert max_length == 100
    foo_bar = parse_option(option, 'foo_bar', 20)
    assert foo_bar == 20
    new_length = parse_option({}, 'new_length', 100)
    assert new_length == 100

if __name__ == "__main__":
    test_parse_option()
