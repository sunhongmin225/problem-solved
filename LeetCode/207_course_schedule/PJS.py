class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = []
        coming_in = [0] * numCourses
        
        for _ in range(numCourses):
            adj.append([])
        
        # make an adjacency matrix for the prerequisites
        for req in prerequisites:
            st, ed = req
            adj[ed].append(st)
            coming_in[st] += 1
        
        queue = []
        for i, deg in enumerate(coming_in):
            if deg == 0:
                queue.append(i)
                
        possible_courses =[]
        
        while(len(queue) != 0):
            curr = queue.pop(0)
            possible_courses.append(curr)
            
            for c in adj[curr]:
                coming_in[c] -= 1
                if coming_in[c] == 0:
                    queue.append(c)
        
        if len(possible_courses) == numCourses:
            return True
        return False
   
