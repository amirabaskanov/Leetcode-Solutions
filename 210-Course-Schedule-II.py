class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Kahn's algorithm

        n = numCourses
        indegrees = [0] * n
        res = []
        g = collections.defaultdict(list)

        for a, b in prerequisites:
            indegrees[a] += 1
            g[b].append(a)

        q = deque()

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            pv = q.popleft()
            res.append(pv)

            for val in g[pv]:
                indegrees[val] -= 1

                if indegrees[val] == 0:
                    q.append(val)

        return res if len(res) == n else [] 
