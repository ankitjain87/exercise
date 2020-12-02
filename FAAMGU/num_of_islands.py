def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = []
        for i in range(m):
            visited.append([False]*n)
        
        def dfs(visited, k, l):
            visited[k][l] = True

            neighbours = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for d in neighbours:
                new_i, new_j = d[0] + k, d[1] + l
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == "1" and not visited[new_i][new_j]:
                    dfs(visited, new_i, new_j)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(visited, i, j)
                    count += 1

        return count 