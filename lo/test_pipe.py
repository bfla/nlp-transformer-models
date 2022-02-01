from lo.pipe import pipe
from lo.fmap import fmap

def test_pipe():
    nums = [1, 2, 3, 4, 5]
    add_num = lambda n: lambda x: n + x
    result = pipe(
        fmap(add_num(10))
    )(nums)
    expected = [11, 12, 13, 14, 15]
    assert result == expected
