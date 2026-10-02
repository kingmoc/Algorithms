#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
	final = []

	for rec_key, rec_value in recipe.items():
		# print(rec_key)
		if rec_key in ingredients:
			amount = ingredients[rec_key] // rec_value
			final.append(amount)
		else:
			return 0
		
	final.sort()
	return final[0]









# print(recipe_batches({ 'milk': 2, 'corn': 3 }, { 'milk': 200 }))
# print(recipe_batches({ 'milk': 2 }, { 'milk': 200 }))
# print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
# print(recipe_batches({ 'milk': 2 }, { 'milk': 200, 'corn': 3 }))
# print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))

# if __name__ == '__main__':
# 	# Change the entries of these dictionaries to test 
# 	# your implementation with different inputs
# 	recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
# 	ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
# 	print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))