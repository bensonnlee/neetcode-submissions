class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        calculate the distances and store the index for every point
        sort the distances, keep the index
        get the indices of the shortest distances
        return the indices of points of the shortest distances

        or just create another list of the points and the distances and just return the points
        """
        for idx, point in enumerate(points):
            points[idx].append(point[0]**2 + point[1] ** 2)

        points.sort(key=lambda x: x[2])

        ans = [point[:2] for point in points][:k]
        return ans