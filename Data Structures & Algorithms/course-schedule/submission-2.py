class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def has_cycle(course) -> bool:
            if course in path:
                return True
            if course in done:
                return False

            path.add(course)
            for prereq in adjList[course]:
                if has_cycle(prereq):
                    return True

            path.remove(course)
            done.add(course)

            return False

        adjList = {}
        for course in range(numCourses):
            adjList[course] = []
        
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])

        done, path = set(), set()

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True
