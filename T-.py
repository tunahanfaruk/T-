variables = {}

while True:
    x = input("<-> ")
    
    
    if x.startswith("write(") and x.endswith(")"):
        content = x[6:-1] 
        
        
        if content in variables:
            print(variables[content])
        else:
            print(content)  
    
    
    elif x.startswith(":") and "&" in x:
        try:
            t = x.index("&")  
            var_name = x[1:t]  
            var_value = x[t+1:] 
            
            
            try:
                var_value = int(var_value)
            except ValueError:
                pass 
            
           
            variables[var_name] = var_value
            print(f"{var_name} = {var_value}")
    
        except Exception as e:
            print(f"please give a new value to variable: {e}")
    
    elif "+" in x:
        pi = x.index("+")
        var1 = x[:pi]
        var2 = x[pi+1:]
        var3 = int(var1) + int(var2)
        print(var3)


    elif "-" in x:
        pi = x.index("-")
        var1 = x[:pi]
        var2 = x[pi+1:]
        var3 = int(var1) - int(var2)
        print(var3)


    elif "*" in x:
        pi = x.index("*")
        var1 = x[:pi]
        var2 = x[pi+1:]
        var3 = int(var1) * int(var2)
        print(var3)


    elif "/" in x:
        pi = x.index("/")
        var1 = x[:pi]
        var2 = x[pi+1:]
        var3 = int(var1) / int(var2)
        print(var3)
    
    elif "^" in x:
        pi = x.index("^")
        var1 = x[:pi]
        var2 = x[pi+1:]
        var3 = int(var1) // int(var2)
        print(var3)


    else:
        print("ERROR unnown command")