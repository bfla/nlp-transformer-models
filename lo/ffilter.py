def ffilter(fn):
  return lambda arr: list(filter(fn, arr))