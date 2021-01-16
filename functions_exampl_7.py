#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
We wanted
1) user friendly way
2) dictionary
3) json
4) no-sql database

Solution is

Keyword only arguments
'''

def my_ssh(host,port=123,*cmds,datacenter_loc,dc_name): 
    print("commands received : ",cmds)
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    print("datacenter_loc : ",datacenter_loc)
    print("dc_name :",dc_name)
    return host

result = my_ssh("192.168.1.10",123,"ls","dir",dc_name="IDC",datacenter_loc="India")
print("result : ",result)

# ex: print(file=,sep=,flush=)

D={"dc_name":"IDC","datacenter_loc":"India"}

result = my_ssh("192.168.1.10",123,"ls","dir",**D) # UNPACKING
print("result : ",result)

