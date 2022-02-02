from lo.flatten import flatten
from lo.fmap import fmap
from lo.pipe import pipe

def flat_map(fn, depth = 1):
    return lambda arr: pipe(flatten(depth = depth), fmap(fn))(arr)