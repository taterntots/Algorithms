#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0

  for key in ingredients:
    # print(ingredients[key])
    # if recipe[key] < -1:
    #   return 1

    # If required recipe ingredients is less than available ingredients
    while recipe[key] < ingredients[key]:
      # add one to the batch_number
      batches += 1
      # remove the number of ingredients used from available ingredients
      ingredients[key] -= recipe[key]
      print(ingredients[key])

  # Return the maximum number of batches we can make with the available ingredients
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 532, 'butter': 248, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))