#yairvinsh 


def polindrom(args): 
    if len(args) != 4: 
        raise("not the right length of charecters")
    l = ""
    args = args.lower()
    
    for i in args:
        if i.isalnum(): 
            l += i 
            
    if l == l[::-1]: 
        return True 
    else: 
        return False 
        
args = input("enter a sequence of characters:")

print(polindrom(args))