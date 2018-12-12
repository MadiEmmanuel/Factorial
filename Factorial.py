
def fact(n):
    f=1
    if num  >= 1:
        for i in range(1, n+1):
            f=f*i
            
    elif   num < 1:
            print("Enter positive intergers only")

    else:
            print("Enter numeric numbers only") 
              
    return f    
        
    
    
num = int(input("Enter number:"))

result = fact(num)
       
print(result)

import unittest
from factorial import fact
    
    
   
   
  
