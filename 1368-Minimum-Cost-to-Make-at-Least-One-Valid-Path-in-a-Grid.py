class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cost = 0

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        dist = [[float("inf")] * n for _ in range(m)] # distance matrix with inf
        dist[0][0] = 0

        q = deque([(0, 0)])

        while q:
            i, j = q.popleft()
            for p, (dr, dc) in enumerate(directions, start=1): # match 1234 to the directions
                nr = i + dr # new row
                nc = j + dc # new column & decided to keep i, j from my nested loop earlier approach
                if 0 <= nr < m and 0 <= nc < n:
                    price = 0 if grid[i][j] == p else 1
                    new_cost = dist[i][j] + price
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if price == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
        return dist[m - 1][n - 1]
