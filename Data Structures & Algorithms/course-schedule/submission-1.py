class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if numCourses is None: # no courses
            return False # no courses to take
        
        if not prerequisites: # no prereqs
            return True # its possible to take all courses
        
        # not undirected edges, directed edges
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        
        for prereq in prerequisites:
            course1, course2 = prereq
            graph[course1].append(course2)
        
        # now all courses are mapped to their prereqs

        visited = set()
        current_path = set()

        def dfs(node):

            if node in current_path:
                return False # in this path we visited this node already and seeing it again is a cycle

            if node in visited:
                return True # we already visited this and made sure there was no cycle

            current_path.add(node)
            visited.add(node)

            for child in graph[node]:
                if not dfs(child):
                    return False
            
            current_path.remove(node)
            return True
            



        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True