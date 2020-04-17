#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if cache is None:
    cache = {}

  # Set up base cases: 
  if n == 0: # if cookie monster eats zero cookies
    return 1
  elif n == 1: # if cookie monster eats one cookie
    return 1
  elif n == 2: # if cookie monster eats two cookies (only two combos - 2, 11)
    return 2
  elif n == 3: # if cookie monster eats three cookies (only four combos - 1111, 12, 21, 31)
    return 4

  # Set up cache
  elif cache and cache[n]:
    return cache[n]
    
  # Actual logic for calculating cookie pulls
  else:
    cache[n] = eating_cookies(n-1, cache)+ eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

print(eating_cookies(5))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')