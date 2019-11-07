#!/usr/bin/python

import argparse

def find_max_profit(prices):
	crr_min_price = 0
	max_profit = 0
	x = [0]

	for i in range(1, len(prices)):
		crr_min_price = prices[i-1]

		if max_profit > 0 and prices[i] - crr_min_price < 0:
			return max_profit
		elif max_profit > 0:
			max_profit += prices[i] - crr_min_price
			return max_profit
		# elif max_profit < 0:
		# 	x.append(prices[i] - crr_min_price)
		# 	print(x, "negative profits")
		max_profit = (prices[i] - crr_min_price)


	return max_profit


# print(find_max_profit([1050, 270, 1540, 3800, 2])) # Can't Pass 3530
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79])) # Can't Pass 94


# print(find_max_profit([105, 27, 154, 380, 20])) #special
# print(find_max_profit([10, 7, 5, 8, 11, 9]), "---- 1 ----")

# print(find_max_profit([7,5,3,1]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]), "---- 2 ----")
# print(find_max_profit([100, 99, 80, 50, 20, 10]), "---- 2 ----")

# print(find_max_profit([100, 55, 4, 98]))
# print(find_max_profit([2, 4, 6]), "---- 3 ----")

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))