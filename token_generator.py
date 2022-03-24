# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:45:31 2020
@author: msaka-git
"""


from uuid import uuid4
import time
import pickle
import os
l=''



def token_create():
    
    
    rand_token=uuid4()
    global l
    l=str(rand_token)
    
    pickle.dump(l,open("save.p","wb"))
   
    return l
    
   
def return_token():
    print(l)
    
 
if __name__ == '__main__':
    token_create()
    return_token()

    time.sleep(70)
   
    os.remove("save.p")
