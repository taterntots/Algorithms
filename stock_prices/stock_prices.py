#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # # Sort the list from smallest to largest price
  # prices.sort()
  # # Find the largest and smallest price in the list and assign them values
  # largest_price = prices[-1]
  # smallest_price = prices[0]
  # # Calculate the difference between the smallest and largest price to find the max profit price
  # max_profit = largest_price - smallest_price

  # Create variables for current minimum price and current maximum profit. Set current min and current max to first index
  curr_minimum = prices[0]
  max_profit = 0
  # Profit is found by subtracting some price with another price that comes before it
  # Loop through the list
  for i in range(len(prices)-1):
  # Profit is equal to (i + 1) minus the current minimum
    profit = prices[i+1] - curr_minimum

  # conditionals
  # if profit is greater than max_profit
  # assign profit to max_profit

    if profit > max_profit or (max_profit == 0 and profit < 0):
      max_profit = profit
    if curr_minimum > prices[i+1]:
      curr_minimum = prices[i+1]

  return max_profit


prices = [110, 67, 49, 382, 209]

print(f'Max Profit: ', find_max_profit(prices))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))