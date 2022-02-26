from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:        
        queue = []
        incoming = [None]*len(recipes)

        for item in supplies:
            queue.append(item)
        
        assert len(recipes) == len(ingredients)
        
        for index, item in enumerate(ingredients):
            incoming[index] = len(item)
        
        possible_recipes = []


        while(len(queue) != 0):
            curr = queue.pop(0)
            if curr not in supplies:
                possible_recipes.append(curr)

            for index, ingredient in enumerate(ingredients):
                if curr in ingredient:
                    incoming[index] -= 1
                    if incoming[index] == 0:
                        queue.append(recipes[index])

            
        
        # should remove supplies from possible_recipes
        possible_recipes = list(set(possible_recipes) - set(supplies))

        return possible_recipes


if __name__ == "__main__":
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]

    print(Solution().findAllRecipes(recipes, ingredients, supplies))