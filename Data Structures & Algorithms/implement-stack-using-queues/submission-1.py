class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            value_to_move = self.q.popleft()
            self.push(value_to_move)
        return self.q.popleft() # what we do is move all elements instead of the last one which we need to '
        # move so like this [1,2,3,4] if we need to pop in a stack but this is a queue we move them so its 
        # like this [4,1,2,3] now we can popleft the 4

        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()