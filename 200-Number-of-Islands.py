class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class Solution:
            if not grid:
                return 0

            rows, cols = len(grid), len(grid[0])
            visited = set()
            islands = 0

            def bdfs(r, c):
                q = deque()
                visited.add((r, c))
                q.append((r, c))
                while q:
                    row, col = q.popleft()
                    directions = 
                    for dr, dc in directions:
                        r, c = row + dr, c + dc


            for r in rows:
                for c in cols:
                    if grid [r][c] == "1" and (r, c) not in visited:
                        bfs(r, c)
                        islands+=1
            return islands
