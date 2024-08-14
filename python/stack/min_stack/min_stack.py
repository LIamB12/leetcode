class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            raise Exception("Cannot get min of empty stack")
        return self.mins[-1]

