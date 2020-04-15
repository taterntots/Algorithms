#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Sort the list from smallest to largest price
  prices.sort()
  # Find the largest and smallest price in the list
  largest_price = prices[-1]
  smallest_price = prices[0]
  # Calculate the difference between the smallest and largest price to find the max profit price
  max_profit = largest_price - smallest_price

  return max_profit

prices = [110, 67, 49, 382, 209]

print(find_max_profit(prices))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))