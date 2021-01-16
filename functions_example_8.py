#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
We are reading from json/no-sql-db/dict -- But we dont know how many args are comming

Solution:
Variable KEYWORDONLY args
'''

def my_ssh(host,port=123,*cmds,datacenter_loc,dc_name,**more_info): 
    print("commands received : ",cmds)
    print("more keyword only args : ",more_info)
    
    print("Executing command on host : ",host)
    print("Executing command on host : ",port)
    print("datacenter_loc : ",datacenter_loc)
    print("dc_name :",dc_name)
    return host

result = my_ssh("192.168.1.10",123,"ls","dir",dc_name="IDC",datacenter_loc="India")
print("result : ",result)

D={"dc_name":"IDC","datacenter_loc":"India"}

result = my_ssh("192.168.1.10",123,"ls","dir",**D) # UNPACKING
print("result : ",result)

D={"dc_name":"IDC","datacenter_loc":"India","dc_zone":"IZone","dc_ops":"idc_team"}

result = my_ssh("192.168.1.10",123,"ls","dir",**D) # UNPACKING
print("result : ",result)


