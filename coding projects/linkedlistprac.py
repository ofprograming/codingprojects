class Node:
    def __init__(self, value, next = None):
        self.value = value 
        self.next = next 
            
def countNodes(head):
    count = 1
    temp = head 
    MysetNum = set()
    while temp.next != None and temp.next.value not in MysetNum and temp.next != temp:
        count += 1  
        MysetNum.add(temp.value)
        temp  = temp.next 
    return count 


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next= node2
node2.next = node3
node3.next = node4
node4.next = node5




def lnode(head): 
    if not head or not head.next:
        return False
    s1= head
    s2 = head
    
    while s2 and s2.next: 
        s1 = s1.next
        s2 = s2.next.next 
        if s1 == s2: 
            return True
        
    return False

def k_List_change(head, k): 
    if k <= 0: 
        return head 
    count = 0 
    temp = head
    placeHolder = 0 
    while temp:
        temp = temp.next 
        count+=1
    temp = head 
    klen = count - k 
    for i in range (klen - 1):
        temp = temp.next
    result = temp.next
    placeHolder = temp 
    temp = head
    for i in range(count-1):
        temp = temp.next  
    temp.next = head 
    placeHolder.next = None 
    return result 
         
        
def plist(head):
    tempo = head
    while tempo.next != None: 
        print(tempo.value,end=' -> ')
        tempo = tempo.next
    print(tempo.value,end=' -|\n')
plist(node1)
     
plist(k_List_change(node1, 5))
         
    
    




def reversenode(head):
    prev = None
    curr = head 
    while curr: 
        nxt = curr.next 
        curr.next = prev
        prev = curr 
        curr = nxt 
    return prev 
     

    
     
    class Solution(object):
        def generate(self, r):
         output = [[1]]
         for i in range(2,r+1): 
            temp =[1]
            for j in range(1, i-1):
                temp.append(output[-1][j] + output[-1][j - 1])
            temp.append(1)
            output.append(temp)
            return output
     
    
     

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2: 
            return None 

        s1, s2 = [], []

        while l1: 
           s1.append(l1.val)
           l1 = l1.next 
        while l2: 
            s2.append(l2.val)
            l2 = l2.next 
        
        reminder, nextnode = 0, None
        while s1 or s2 or reminder: 
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0

            reminder, val = divmod(v1 + v2 + reminder, 10)
            node = ListNode(val, nextnode)
            nextnode = node 

        
