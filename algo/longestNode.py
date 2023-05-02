from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n)]
    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)

    distances = [-1] * n  # 최단 거리를 저장할 리스트
    distances[0] = 0  # 시작 노드의 최단 거리는 0

    q = deque([0])
    while q:
        curr = q.popleft()
        for neighbor in graph[curr]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[curr] + 1
                q.append(neighbor)

    max_distance = max(distances)
    answer = distances.count(max_distance)

    return answer