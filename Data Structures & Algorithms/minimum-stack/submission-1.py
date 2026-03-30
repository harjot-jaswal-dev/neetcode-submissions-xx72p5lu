class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            minimum = val
            self.stack.append((val, minimum))
        elif self.stack[-1][1] > val:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))
        

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][1]
        
