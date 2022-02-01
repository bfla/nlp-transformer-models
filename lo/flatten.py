from itertools import chain
from functools import reduce

def is_flattenable(thing):
    if isinstance(thing, list):
        return True
    return False

# See: https://github.com/lodash/lodash/blob/master/.internal/baseFlatten.js
def base_flatten(arr, depth, predicate = is_flattenable, result = []):
    if arr == None:
        return result
    if len(arr) == 0:
        return result
    if not predicate(arr):
        return result
    for i in arr:
        if depth > 0 and predicate(i):
            if (depth > 1):
              base_flatten(i, depth - 1, predicate = predicate, result = result)
            else:
              result.extend(i)
        else:
            result.append(i)
    return result

def flatten(depth = 1):
    return lambda arr: base_flatten(arr, depth, result = [])