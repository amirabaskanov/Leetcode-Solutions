class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = {}
        for i in range(len(points)):
            d = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
            distances[i] = d
        distances = sorted(distances, key=lambda x: distances[x])

        res = []
        if k == 0:
            return res
        else:
            for j in range(k):
                index = distances[j]
                res.append(points[index])
        return res

# my Solution
