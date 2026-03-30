class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
         # key word minimum points me towards bfs
         
        start = "0000"
        queue = deque()
        queue.append("0000")
        visited = set()
        visited.add("0000")
        turns = 0

        if start in deadends:
            return -1

        while queue:
            
            for i in range(len(queue)):
                state = queue.popleft()

                if state == target:
                    return turns

                for i in range(4): # len 4 since we have 4 positions,

                    curr_wheel = int(state[i])

                    curr_wheel_up = (curr_wheel + 1) % 10
                    curr_wheel_down = (curr_wheel - 1) % 10

                    before = state[:i]
                    after = state[i + 1:]
                    curr_up = str(curr_wheel_up)
                    curr_down = str(curr_wheel_down)

                    final_up = before + curr_up + after
                    final_down = before + curr_down + after

                    if final_up not in deadends and final_up not in visited:
                        queue.append(final_up)
                        visited.add(final_up)
                    
                    if final_down not in deadends and final_down not in visited:
                        queue.append(final_down)
                        visited.add(final_down)

            turns += 1 # do i needed nested loops to get the turn incrementation right?
        
        return -1

            

        

                
                


