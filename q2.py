# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:00:17 2020

@author: ASUS
"""
ref=[]
f=[]
pge_flt=0
f_no=0
y=-1
import random
for x in range(100):
    y=random.randrange(0,9)
    ref.append(y)
#ref=[1,2,3,4,5,6,7,8,9]
print("reference string is ",ref)
for x in range(len(ref)):
    if ref[x] not in f:
        pge_flt=pge_flt+1
        if(len(f)!=7):
            f.append(ref[x])
            print(f)
        else:
            if(f_no==7):
                f_no=0
            f_no=f_no+1
            f[f_no-1]=ref[x]  
            print(f)    
print("page fault is",pge_flt)   
        
"""if ref[x] not in f:
        pge_flt=pge_flt+1
        #if x>6:
        if(len(f)<7) :
            f_no=f_no+1
            print(f_no," ",ref[x])
            f[f_no-1]=ref[x]
        elif(len(f)<7 & y<7):
            f.append(ref[x])
            y=y+1            
            print("the values stored in frames is " ,f)
            print("values of x ",x,"values of f ",len(f))
            if y==7:
                f_no=0
    else:
        pass"""        

            