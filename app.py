import array
import numpy as np
#import pandas as pd

def mnx():
    n=int(input("enter matrix dimensions: "))
    m=np.zeros((n,n))
    for i in range(len(m)):
            for j in range(-1,len(m)):
                l=i+1
                m[i][i]=l
            
    print(m)
    print("Yeh!! you completed your task")
    
mnx()

