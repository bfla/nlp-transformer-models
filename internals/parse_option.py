def parse_option(options, key, default = None):
  if key in options:
    return options[key]
  return default