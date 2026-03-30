class Graph:
    
    def __init__(self):

        self.maps = {}


    def addEdge(self, src: int, dst: int) -> None:

        if src not in self.maps:
            self.maps[src] = []
        if dst not in self.maps:
            self.maps[dst] = []
        
        if dst not in self.maps[src]:
            self.maps[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:

        if src in self.maps:
            if dst in self.maps[src]:
                self.maps[src].remove(dst)
                return True
        
        return False



    def hasPath(self, src: int, dst: int) -> bool:

        # assume they exist in graph/maps

        visited = set()
        visited.add(src)


        def dfs(current, target, visited):

            if current == target:
                return True


            for neighbor in self.maps[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor, target, visited):
                        return True
            
            return False
                    

        return dfs(src, dst, visited)
