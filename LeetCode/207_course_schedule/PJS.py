# topological sort...?

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = []                        # adjacency list
        coming_in = [0] * numCourses    # degree of incoming nodes for a certain node
        
        for _ in range(numCourses):
            adj.append([])
        
        # make an adjacency matrix for the prerequisites
        for req in prerequisites:
            st, ed = req
            adj[st].append(ed)
            coming_in[ed] += 1
        
        queue = []
        # put the course with incoming degree 0 to the queue
        # if incoming degree is 0, it means there are no prerequisites for that course
        for i, deg in enumerate(coming_in):
            if deg == 0:
                queue.append(i)
        
        possible_courses =[]
        
        # until queue becomes empty...
        #   - take a course from the queue, and for its adjacent courses, decrease their incoming degree
        while(len(queue) != 0):
            curr = queue.pop(0)
            possible_courses.append(curr)
            
            for ed in adj[curr]:
                coming_in[ed] -= 1
                if coming_in[ed] == 0:
                    queue.append(ed)
        
        if len(possible_courses) == numCourses:
            return True
        return False
