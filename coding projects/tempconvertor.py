#YAIRVINSH
def funcOfTemp(v): 
    try:
        if "c" not in temp and "f" not in temp: 
            raise SyntaxError("not a valid character")
        temp_val = float(temp[:-1])
    
    
        if "c" in temp: 
            return (temp_val * 1.8) +32 
        if "f" in temp:
            return (temp_val - 32)/ 1.8
    except ValueError: 
        raise("not a valid number")
        
temp = input("please enter a tempeture (number)(indicator):")

result = funcOfTemp(temp.lower())
print(f"the result is: {result}")
    
        
    
            
    
    
    