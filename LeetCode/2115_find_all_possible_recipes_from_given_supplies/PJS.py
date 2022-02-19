# topological sort

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = {}        # adjacency list (as a dictionary)
        in_degree = {}  # keeps in-degree
        
        # make an adjacency matrix
        for i, tgt in enumerate(recipes):
            ingredients_for_tgt = ingredients[i]
            for ingredient in ingredients_for_tgt:
                if ingredient in adj and tgt not in adj[ingredient]:
                    adj[ingredient].append(tgt)
                else:
                    adj[ingredient] = [tgt]
                
                if tgt in in_degree:
                    in_degree[tgt] += 1
                else:
                    in_degree[tgt] = 1
        
        queue = supplies
        possible_recipes = []
        
        while(len(queue) != 0):
            curr = queue.pop(0)
            if curr in recipes:
                possible_recipes.append(curr)
            
            if curr in adj:
                for tgt in adj[curr]:
                    in_degree[tgt] -= 1
                    if in_degree[tgt] == 0:
                        queue.append(tgt)
        
        return possible_recipes
