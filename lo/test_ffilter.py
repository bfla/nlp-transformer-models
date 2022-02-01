from lo.ffilter import ffilter

def test_ffilter():
    nums = [1, 2, 3, 4, 5]
    my_filter = lambda x: x == 3
    result = ffilter(my_filter)(nums)
    expected = [3]
    assert result == expected
