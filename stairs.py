class Solution(object):
    def climbStairs(self, n):
        if n <=2: 
            return n
        a, b = 1,2  
        for i in range(2, n): 
            temp = b
            b = a+b 
            a = temp  
        return b 
            