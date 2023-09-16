class Solution(object):
    def calPoints(self, operations):
     stack = []
     r = 0 
     for op in operations: 
        if op == "C": 
           r -= stack.pop()
        elif op == "D": 
            stack.append(stack[-1]*2)
            r+= stack[-1]
        elif op == "+": 
            stack.append(stack[-1] + stack[-2])
            r+= stack[-1]
        else: 
            stack.append(int(op))
            r += stack[-1]    
     return r 