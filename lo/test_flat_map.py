from lo.flat_map import flat_map

def test_flat_map():
    nums = [1, [2, 3], 4, 5]
    square = lambda x: x * x
    result = flat_map(square, 1)(nums)
    expected = [1, 4, 9, 16, 25]
    assert result == expected
