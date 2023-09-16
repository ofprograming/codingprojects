class Solution(object):
    def isValid(self, s):
        stack = []
        mappings = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mappings:  
                if not stack or stack[-1] != mappings[char]:
                    return False
                stack.pop()
            else:  
                stack.append(char)
        
        return not stack
