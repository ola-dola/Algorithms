#!/usr/bin/python

import argparse

def find_max_profit(prices):
  potential_max = []

  for i in range(len(prices)):
    if i < len(prices) - 1:
      #compute price diff between bought at price[i] and subsequent prices
      price_diff = [rest - prices[i] for rest in prices[i+1:]]

      #calculate max profit at that price
      max_for_each = max(price_diff)

      #add to list of potential max profits
      potential_max.append(max_for_each)
  
  return max(potential_max)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))