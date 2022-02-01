from lo.fmap import fmap

def test_fmap():
    nums = [1, 2, 3, 4, 5]
    square = lambda x: x * x
    result = fmap(square)(nums)
    expected = [1, 4, 9, 16, 25]
    assert result == expected
