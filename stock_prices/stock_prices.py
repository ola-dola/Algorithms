#!/usr/bin/python

import argparse

def find_max_profit(prices):
  min_so_far = prices[0]
  potential_max = 0
  max_so_far = 0

  for price in prices:
    min_so_far = min(min_so_far, price)
    potential_max = price - min_so_far
    max_so_far = max(max_so_far, potential_max)

  return max_so_far

     

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))