class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for idx, point in enumerate(points):
            points[idx].append(point[0]**2 + point[1] ** 2)

        points.sort(key=lambda x: x[2])

        ans = [point[:2] for point in points][:k]
        return ans