class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.ministack) == 0:
            self.ministack.append(val)
        else:
            curmini = min(val, self.ministack[-1])
            self.ministack.append(curmini)
        

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
        #O(n)
        # mini = self.stack[0]
        # for num in self.stack:
        #     if num < mini:
        #         mini = num
        # return mini
        
