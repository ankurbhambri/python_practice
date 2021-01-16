#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Need to write a function which take command as an arguments
def my_ssh(host,port=123,cmd1)
def my_ssh(host,port=123,cmd1,cmd2)
def my_ssh(host,port=123,cmd1,cmd2,cmd3)
But we dont know how commands are coming,
In that scenario we have option called 

VARIABLE ARGUMENTS

'''
def my_ssh(host,port=123,*cmds): 
    print("commands received : ",cmds)
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    return host

result = my_ssh("192.168.1.10")
print("result : ",result)


# In[4]:



def my_ssh(host,port=123,*cmds): 
    print("commands received : ",cmds)
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    return host

result = my_ssh("192.168.1.10",123,"ls")
print("result : ",result)


# In[5]:


def my_ssh(host,port=123,*cmds): 
    print("commands received : ",cmds)
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    return host

result = my_ssh("192.168.1.10",123,"ls","dir")
print("result : ",result)


# In[ ]:




