def get(dictionary, key, default = None):
  if key in dictionary:
    return dictionary[key]
  return default