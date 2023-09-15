#operations = ["5","2","C","D","+"]
#def calPoints(operations):
#    stack = []
#    r = 0 
#    for op in operations: 
#        if op == "C": 
#           op -= stack.pop()
#        elif op == "D": 
#            stack.append(operations[op]*2)
#        elif op == "+": 
#            stack.append(operations[op-2] + operations[op-1])
#            r+= stack[-1]
#        else: 
#            stack.append(int(op))
#            r += stack.append(stack[-1])    
#    return r 
#
#print(calPoints(operations))
     
     

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
           
def inorder(tree): 
    if tree != None: 
        return inorder(tree.left) + [tree.val] + inorder(tree.right) 
    else : 
        return [] 
              
t0 = TreeNode(10)
t1 = TreeNode(5)
t2 = TreeNode(8,t0,t1)
t3 = TreeNode(1)
t4 = TreeNode(9)
t5 = TreeNode(12,t4,t3)
t6 = TreeNode(2,t5,t2)

            
print(inorder(t6))

def recu(lis): 
    if lis == 1: 
        return [1] 
    return [lis] + recu(lis - 1)

