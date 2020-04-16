#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  # Create a variable for batches
  batches = 0
  batch_list = []

  # If length of the recipe dictioniary is greater than ingredients, dont bother
  if len(recipe) > len(ingredients):
    return 0

  # Loop through the dictionaries
  for key in ingredients:
      # Append the batch items to the batch_list
      batch_list.append(ingredients[key] // recipe[key])
  
  # Sort the batch_list so that the smallest value (our total feasable batch run) is index zero
  batch_list.sort()
  print(batch_list)

  # Declare batchlist at index zero as our number of batches
  batches = batch_list[0]
  print(batches)

    # # If required recipe ingredients is less than available ingredients
    # while recipe[key] < ingredients[key]:
    #   # add one to the batch_number
    #   batches += 1
    #   # remove the number of ingredients used from available ingredients
    #   ingredients[key] -= recipe[key]
    #   # print(ingredients[key])
    #   # print (ingredients[key] // recipe[key])
      

  # Return the maximum number of batches we can make with the available ingredients
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
