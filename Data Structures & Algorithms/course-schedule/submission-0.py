class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = {}

        for prereq in prerequisites:
            course, prereq_course = prereq
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq_course)

        visited = set()
        visiting = set()

        def dfs(course):

            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            if course not in graph:
                return True
            
            visiting.add(course)

            for pre in graph[course]:
                if not dfs(pre): # this is false
                    return False
            
            # checked all prereqs, remove from visiting add to visited
            visiting.remove(course)
            visited.add(course)

            return True
            


        for course in range(numCourses):
            if not dfs(course): # is False
                return False
        
        return True