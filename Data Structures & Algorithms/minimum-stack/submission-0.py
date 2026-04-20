class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_value) == 0 or  val < self.min_value[-1]:
            self.min_value.append(val)
        else:
            self.min_value.append(self.min_value[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_value[-1]
        
