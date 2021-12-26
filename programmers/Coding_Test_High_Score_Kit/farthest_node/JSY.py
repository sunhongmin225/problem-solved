from collections import deque

MAX = 50001

def solution(n, edge):
    # 1. edge to linked list
    # ? how to update with multiple keys
    graph = {}
    key_values_dict = ((i, []) for i in range(1, n + 1))
    graph.update(key_values_dict)

    for item in edge:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])
        

    # 2. Initialization for BFS
    # QUEUE
    q = deque([])     # ? Python queue
    q.append(1)
    # visited 
    visited = [-1] * (n + 1)
    visited[1] = 1
    # min_length
    min_length = [MAX] * (n + 1)
    min_length[1] = 0

    # 3. BFS
    while len(q) > 0:
        target = q.pop()
        
        for neighbor in graph[target]:

            if visited[neighbor] == -1:
                q.append(neighbor)
                
                visited[neighbor] = 1
                min_length[neighbor] = min_length[target] + 1
    
                
    # 4. Find the max and the number of nodes with the max value
    max = min_length[1]
    for i in range(1, n + 1):
        if min_length[i] > max:
            max = min_length[i]
    
    cnt = 0
    for item in min_length:
        if item == max:
            cnt += 1
    
    return cnt




if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    solution(n, edge)
    