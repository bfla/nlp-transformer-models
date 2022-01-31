from types import SimpleNamespace
from server import token_serializer

# content of test_sample.py
def func(x):
    return x + 1


def test_token_serializer():
    token = SimpleNamespace()
    token.text = 'hello'
    token.pos_ = 'ADJ'
    token.tag_ = 'foo'
    token.dep_ = 'bar'
    token.idx = 5
    token.prob = 0.75
    actual = token_serializer(token)
    assert type(actual) == dict