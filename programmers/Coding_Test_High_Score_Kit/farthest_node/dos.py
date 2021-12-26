from collections import deque

def solution(n, edge):
    distances = {i:0 for i in range(1, n+1)}
    adjacency = {i:[] for i in range(1, n+1)}
    for u,v in edge:
        adjacency[u].append(v)
        adjacency[v].append(u)
    dq = deque(adjacency[1])
    distance = 1
    while dq:
        for _ in range(len(dq)):
            u = dq.popleft()
            if distances[u] == 0:
                distances[u] = distance
                for v in adjacency[u]:
                    dq.append(v)
        distance += 1

    del distances[1]
    max_distance_from_firstnode = max(distances.values())
    answer = 0
    for _, distance in distances.items():
        if distance == max_distance_from_firstnode:
            answer += 1

    return answer


if __name__=="__main__":
    n = 6
    edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    print(
        solution(n, edges)
    )