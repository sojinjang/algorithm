def solution(n, computers):
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)

    num_networks = 0
    visited = [False for _ in range(n)]

    for start_comp in range(n):
        if not visited[start_comp]:
            dfs(start_comp)
            num_networks += 1

    return num_networks
