"""
1. Should recap on data structures for building graphs (adjacency matrix / adjacency list)
2. First time implementing topological sort. 
3. One can use topological sort to find cycle in a directed graph. 
"""

from typing import List

class Solution:
    # Add Graph Class
    class Graph:
        '''
        Represented as an adjacency list; 
        dict[int, set[int]]
        '''
        def __init__(self, num_vertices: int) -> None:
            self.graph = dict([])
            self.V = num_vertices

        def add_node(self, node_to_add: int) -> None:
            if self.graph.get(node_to_add) is None:
                self.graph[node_to_add] = set([])

        def add_edge(self, src: int, dest: int) -> None:
            self.add_node(src)
            self.add_node(dest)
            self.graph[src].add(dest)
        
        def get_nodes(self) -> List:
            return [node for node in self.graph]

        def find_cycle(self, start_node: int) -> bool:
            '''
            start_node로 향하는 cycle이 있는지 확인한다. 
            '''
            visited = [False for _ in range(self.V)]

            value = self.dfs(start_node, visited)
            print(value)
            return value

        def dfs(self, node, visited):
            print(node, visited)
            for neighbor_node in self.graph[node]:
                print(self.graph[node])
                if visited[neighbor_node] is False:
                    visited[neighbor_node] = True
                    return self.dfs(neighbor_node, visited)
                else:
                    return True
                
                visited[neighbor_node] = False

            return False
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build a graph
        graph = self.Graph(numCourses)
        for after, before in prerequisites:
            # after, before: ai(dest), bi(src)
            graph.add_edge(before, after)
        print(graph.graph)

        # 2. Traverse the graph via DFS. 
        has_cycle = False
        '''
        루트에서만이 아닌, 모든 노드에서 다 확인을 하도록 구현한 이유: 
        루트 노드가 어디인지 주어지지 않았기 때문. 
        '''
        for node in graph.get_nodes(): 
            # print(node)
            if graph.find_cycle(node): # find a cycle starting from node
                has_cycle = True
                break
        
        return not has_cycle
            

if __name__ == "__main__":
    numCourses = 3
    prerequisites = [[1,0],[2,0],[0,2]]

    print(Solution().canFinish(numCourses, prerequisites))