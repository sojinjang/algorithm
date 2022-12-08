from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [1, 2, 4],
    [1, 8],
    [1, 4],
    [3, 6, 7],
    [3],
    [7, 8],
    [2, 3, 8],
    [5, 7]
]
visited = [False] * 9
bfs(graph, 1, visited)
