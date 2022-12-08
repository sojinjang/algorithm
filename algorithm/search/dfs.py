def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)
