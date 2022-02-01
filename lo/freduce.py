from functools import reduce

def freduce(fn, initial_state):
  return lambda arr: reduce(fn, arr, initial_state)