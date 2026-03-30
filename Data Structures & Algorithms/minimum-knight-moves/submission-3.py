from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))
        total = 0
        x = abs(x)
        y = abs(y)

        while queue:

            for i in range(len(queue)):

                r, c = queue.popleft()

                if r == x and c == y:
                    return total
                
                moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
                for move in moves:
                    mr, mc = move
                    if (r + mr, c + mc) in visited:
                        continue
                    
                    if r + mr < -2 or c + mc < -2: # we can go slightly negative 
                        continue # 
                    
                    if r + mr > x + 2 or c + mc > y + 2:
                        continue # we don;t want to go away from traget/overshoot it
                    
                    queue.append((r + mr, c + mc))
                    visited.add((r + mr, c + mc))
            
            total += 1
        
        return total

        