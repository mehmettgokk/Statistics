import random

def weighted_srs(data, n, weights, with_replacement=false):
  if weights is None and not with_replacement=False:
    return random.sample(data, n)
  return random.choices(data, weights = weights, k=n)
