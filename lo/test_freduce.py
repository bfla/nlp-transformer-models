from lo.freduce import freduce

def test_freduce():
    nums = [1, 2, 3, 4, 5]
    my_reducer = lambda acc,x: acc + x
    result = freduce(my_reducer, 0)(nums)
    expected = 15
    assert result == expected