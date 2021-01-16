#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
map builtin function
'''

def my_func(ip):
    return ip+":8080"

L = ["192.168.1.10","192.168.1.11","192.168.1.12","192.168.1.13"]

# Using For Loop
result=[]
for i in L:
    r = my_func(i)
    result.append(r)

print("result : ",result)


# In[4]:


'''
map builtin function
'''

def my_func(ip):
    return ip+":8080"

L = ["192.168.1.10","192.168.1.11","192.168.1.12","192.168.1.13"]

result = map(my_func,L)
print("result : ",list(result))


# In[5]:


'''
Lambda Functions:
- are functions
- doesn't have name
- one liner
- We embed inside func argument
- We can us in comprehensions(need to discuss)
- We can also assign to varaible
'''


# In[7]:


'''
using lambda and map
'''
L = ["192.168.1.10","192.168.1.11","192.168.1.12","192.168.1.13"]

'''
def my_func(ip): 
    return ip+":8080"

# Equellent lambda

lambda (ip): ip+":8080"
'''

result = map(lambda ip: ip+":8080",L)

print("result : ",list(result))


# In[8]:


'''

Filter only production servers
'''

servers = ["pserver","pserver","pserver","tserver","dserver"]

result=[]
for i in servers:
    if i.startswith("p"):
        result.append(i)
print("result : ",result)


# In[9]:


'''
filter function
Filter only production servers
'''

def my_filter(s):
    if s.startswith("p"):
        return True
    else:
        return False

servers = ["pserver","pserver","pserver","tserver","dserver"]

result = filter(my_filter,servers)
print("result : ",list(result))


# In[10]:


'''
We can assign lambda to variable
'''

f = lambda a,b : a+b

'''
Equellent
def f(a,b):
    return a+b
'''
result = f(10,20)
print("result : ",result)


# In[ ]:




