from functools import reduce

def pipe(*fns):
  return lambda init_val: reduce(lambda acc,fn: fn(acc), fns, init_val)