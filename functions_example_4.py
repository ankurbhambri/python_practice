#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Function with default value arguments
'''
def my_ssh(host,port=123): # Oreder need to take care- 1st non-default value then default value args
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    return host

result = my_ssh("192.168.1.10")
print("result : ",result)

result = my_ssh("192.168.1.11",123)
print("result : ",result)

result = my_ssh("192.168.1.12",124)
print("result : ",result)


# In[ ]:




