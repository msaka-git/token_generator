# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:54:27 2020
@author: msaka-git
"""

import pickle,sys

try:
    token_load=pickle.load(open("save.p","rb"))
    
except FileNotFoundError:
    print("You must run TOKEN first.")
    sys.exit()
    
    
def menu():
    
    inp=input("Please enter your userid: ")
    pas=input("Please provide your password: ")
    tok=input("Please enter your token: ")
    
    if inp == 'mufit' and pas == 'abc' and tok == token_load:
        print("Logged in !!!!")
    else: 
        print("NOOOOOOOOOOOOOOOOOOOO")
    
menu()
