"""[summary]
- since n is small(max 100) some sort of brute force approach will be fine
- need a set of unique supplies to evaluate two things.
  1. whether a recipe is in the set
  2. all ingredients for that recipe is in the set
* note that line 19 can be computationally expensive.
"""
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        unique_supplies = set(supplies)
        stuff = set()

        n = len(recipes)

        while n:
            for rcp, ing in zip(recipes, ingredients):
                if rcp not in unique_supplies and all(i in unique_supplies for i in ing):
                    unique_supplies.add(rcp)
                    stuff.add(rcp)
            n -= 1

        return stuff





if __name__=="__main__":
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]

    s = Solution()
    print(s.findAllRecipes(recipes, ingredients, supplies))

    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]

    s = Solution()
    print(s.findAllRecipes(recipes, ingredients, supplies))
    
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]

    s = Solution()
    print(s.findAllRecipes(recipes, ingredients, supplies))
