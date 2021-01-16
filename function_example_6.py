#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
PACKING and UNPACKING
'''

def my_ssh(host,port=123,*cmds): # *cmds --> PACKING
    print("commands received : ",cmds)
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    return host


result = my_ssh("192.168.1.10",123,"ls","dir")
print("result : ",result)

# L=F.readlines()
L=["192.168.1.10",123,"ls","dir"]

#result = my_ssh(L)# COMPLETE LIST WILL GO, IT IS WRONG
#print("result : ",result)

result = my_ssh(L[0],L[1],L[2],L[3]) # THIS IS FINE, DIFFICULT IF LIST HAS MORE ELEMENT
print("result : ",result)

result = my_ssh(*L) # UNPACKING->
print("result : ",result)

