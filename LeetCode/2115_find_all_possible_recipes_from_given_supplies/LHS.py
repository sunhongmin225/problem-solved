## Refer to Week6 PJS code
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        ## make dict containing all recipes, ingredients, supplies
        req = {}
        for recipe in recipes:
            req[recipe] = [0, []]   ## [number of prerequisite of recipe, [list for items that need it]]
        for ingredient in ingredients:
            for each in ingredient:
                if each not in req:
                    # when ingredient is in supplies
                    if each in supplies:
                        req[each] = [0, []]
                    # when ingredient is not in supplies, mark as -1 
                    else:
                        req[each] = [-1, []]
        for supply in supplies:
            if supply not in req:
                req[supply] = [0, []]

        # initialize the graph
        for i, recipe in enumerate(recipes):
            for each in ingredients[i]:
                req[recipe][0] += 1
                req[each][1].append(recipe)

        # if item needs no other items, it can be added to queue
        queue = []
        for item in req:
            if req[item][0] == 0:
                queue.append(item)
        
        pos_recipes = []
        while(len(queue) != 0):
            curr = queue.pop(0)
            pos_recipes.append(curr)
            
            # when item is ready, following items' status update
            for item in req[curr][1]:
                req[item][0] -= 1
                if req[item][0] == 0:
                    queue.append(item)
        ans = []
        for recipe in recipes:
            if recipe in pos_recipes:
                ans.append(recipe)

        return ans

