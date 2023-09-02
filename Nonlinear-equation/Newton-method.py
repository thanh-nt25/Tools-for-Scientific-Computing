import math
import numpy as np
# nhap ham
def func( x ):
    return 3 ** x
 
# nhap dao ham
def derivFunc( x ):
    return np.log(3) * 3**x
 

def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
         
        
        x = x - h
     
    print("The value of the root is : ",
                             "%.4f"% x)
 
# nhap gia tri khoi tao
x0 = 0.5
newtonRaphson(x0)