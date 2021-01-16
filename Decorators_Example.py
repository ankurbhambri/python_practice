#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
If we want to reuse the code then we can write functions
Suppose,
inside the function also, some part of the code we can reuse? then what to do??
'''


# In[2]:


def add1(a,b):
    print("Result is :")
    print(a+b)
    print("End of the Result")

add1(10,20)


# In[3]:


def sub1(a,b):
    print("Result is :")
    print(a-b)
    print("End of the Result")

sub1(10,20)


# In[4]:


def add2(a,b):
    print("Result is :")
    print(a+b)
    print("End of the Result")

add2(10,20)


# In[5]:


'''
Can we write common function where it has common stmts and re-use
'''

def my_common_func():
    print("Result is :")
    print("End of the Result")
    

def add3(a,b):
    my_common_func()
    print(a+b+1)
    my_common_func()
    
add3(10,20) 

'''
my_common_func wont work -- BAD DESIGN
'''


# In[6]:


'''
Design Pattern :- Decorator Pattern
'''


# In[7]:


'''
This is as per the Decorato Pattern
'''
def my_decorator(func_needs_decoration):
    def decorated_func(x,y):
        print("Result is :")
        func_needs_decoration(x,y)
        print("End of the Result")
    return decorated_func


# In[11]:


@my_decorator
def add3(a,b):
    print(a+b+a)

add3(10,20)


# In[12]:


'''
THIS SECTION IS FOR UNDERSTANDING OF DECORATOR. 
'''
def my_decorator(func_needs_decoration): # func_needs_decoration = add4
    def decorated_func(x,y): # f(10,20) # x=10,y=20
        print("Result is :")
        func_needs_decoration(x,y) # add4(10,20)
        print("End of the Result")
    return decorated_func



def add4(a,b):
    print(a+b+a+b)


f = my_decorator(add4)
# f = decorated_func
f(10,20)


# In[ ]:




