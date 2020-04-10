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
i= int(input("enter how many reference nos required"))
import random
for x in range(i):
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
        
       

            
