from lo.flatten import flatten

def test_flatten():
    nums0 = [[1,2], 3, [4], [5, 6, 7]]
    result0 = flatten()(nums0)
    expected0 = [1, 2, 3, 4, 5, 6, 7]
    assert result0 == expected0

def test_flatten_with_depth_one():
    nums1 = [[1,[2]], 3, [4], [5, [6, 7]]]
    result1 = flatten(1)(nums1)
    expected1 = [1, [2], 3, 4, 5, [6, 7]]
    assert result1 == expected1
    
def test_flatten_with_depth_two():
    nums2 = [[1,[2]], 3, [4], [5, [6, 7]]]
    result2 = flatten(2)(nums2)
    expected2 = [1, 2, 3, 4, 5, 6, 7]
    assert result2 == expected2


# if __name__ == "__main__":
#     test_flatten()
