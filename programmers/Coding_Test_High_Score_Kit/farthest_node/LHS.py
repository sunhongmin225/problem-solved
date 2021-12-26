
def solution(n, edge):
    graph = {}
    
    for i in range(len(edge)):
        a = edge[i][0]
        b = edge[i][1]
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]
    # print(graph)

    visit = []   
    queue = []
    start_node = 1
    queue.append(start_node)
    visit.append(start_node)
    dist = [-1]*(n+1)
    dist[1] = 0

    while queue:
        node = queue.pop(0)

        for next_node in graph[node]:
            # print(next_node)
            if next_node not in visit:
                # print(dist[next_node])
                dist[next_node] = dist[node] + 1 
                # print(dist[next_node])
                visit.append(next_node)
                queue.extend(graph[next_node])
    # print(dist)
    maxnum = max(dist)
    # print(dist.count(maxnum))
    return dist.count(maxnum)  


# def bfs(graph, start_node, n):
#     visit = []
#     queue = []
#     queue.append(start_node)
#     visit.append(start_node)
#     dist = [-1]*(n+1)
#     dist[1] = 0
#     # print(dist)

#     while queue:
#         node = queue.pop(0)
        
#         # print("node " + str(node))
#         # print("graph[node]: "+str(graph[node]))
#         for next_node in graph[node]:
#             # print(next_node)
#             if next_node not in visit:
#                 # print(dist[next_node])
#                 dist[next_node] = dist[node] +1 
#                 # print(dist[next_node])
#                 visit.append(next_node)
#                 queue.extend(graph[next_node])
#     # print(dist)
#     maxnum = max(dist)
#     # print(dist.count(maxnum))
#     return dist.count(maxnum)

# def solution(n, edge):
#     graph = {}
    
#     for i in range(len(edge)):
#         a = edge[i][0]
#         b = edge[i][1]
#         graph[a] = graph.get(a, []) + [b]
#         graph[b] = graph.get(b, []) + [a]
#     # print(graph)
#     # print(bfs(graph, 1, n))    
#     return bfs(graph, 1, n)