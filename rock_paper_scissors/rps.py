#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
 
#  # define list of all possible plays and RPS variables
#   rps = ['rock', 'paper', 'scissors']
#   # possible_plays = []

#   # If no players, game does not start
#   if n == 0:
#     return [[]]
#   # If one player, there are only three possibilities
#   elif n == 1:
#     return [rps]
#   # Logic to figure out all possible plays
#   else:
#     base = rock_paper_scissors(n-1)
#     print(f'BASE: ', base)
#     possible_plays = []
#     for each in base:
#       for j in rps:
#         new_each = each.copy()
#         new_each.append(j)
#         possible_plays.append(new_each)
#       # print(f'EACH:', each)

#         # possible_plays += [each + ['rock'], each + ['paper'], each + ['scissors']]
#       # possible_plays.append(each + ['rock'])
#       # possible_plays.append(each + ['paper'])
#       # possible_plays.append(each + ['scissors'])
#       # print(f'PPLAYS', possible_plays)

#     # for p1 in range(len(rps)):
#     #   for p2 in range(len(rps)):
#     #     print(rps[p1], rps[p2])
#     #     possible_plays.append(rps[p1])
  
#   return possible_plays

def rock_paper_scissors(n):

  # define list of all possible plays and RPS variables
  rps = [['rock'], ['paper'], ['scissors']]
  possible_plays = []

  # If no players, game does not start
  if n == 0:
    return [[]]
  # If one player, there are only three possibilities
  elif n == 1:
    return rps

  # Logic to figure out all possible plays
  else:
    base = rock_paper_scissors(n-1)
    for x in base:
      print(f'HOPE THIS WORKS', x + ['rock'], x + ['paper'])
      possible_plays.append(x + ['rock'])
      possible_plays.append(x + ['paper'])
      possible_plays.append(x + ['scissors'])

  return possible_plays

print(f'POSSIBLE PLAYS: ', rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')