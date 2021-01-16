#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 10
def f1():
    x =20
    def f2():
        x =30
        print("In F2 : ",x)
    f2()
    print("In F1 :",x)

f1()
print("Global : ",x)


# In[2]:


x = 10
def f1():
    x =20
    def f2():
        x =30
        print("In F2 : ",locals())
    f2()
    print("In F1 :",locals())

f1()
print("Global : ",locals())


# In[3]:


'''
Local SCOPE
'''
x = 10
def f1():
    x =20
    def f2():
        x =30 # LOCAL SCOPE
        print("In F2 : ",x)
    f2()
    print("In F1 :",x)

f1()
print("Global : ",x)


# In[4]:


'''
Enclosed SCOPE
'''
x = 10
def f1():
    x =20 # Enclosed SCOPE
    def f2():
        print("In F2 : ",x) # using nonlocal keyword for reading is not required
    f2()
    print("In F1 :",x)

f1()
print("Global : ",x)


# In[5]:


'''
Enclosed SCOPE - 2
'''
x = 10
def f1():
    x =20 # Enclosed SCOPE
    def f2():
        # I need to change enclosed scope varaivle value to 200
        # x = 200 --> It will create new varaible in local scope
        nonlocal x # Tells refer enclosed scope varaible
        x =200
        print("In F2 : ",x)
    f2()
    print("In F1 :",x)

f1()
print("Global : ",x)


# In[6]:


'''
Global Scope
'''
x = 10 # Global Scope
def f1():

    def f2():

        print("In F2 : ",x)
    f2()
    print("In F1 :",x)

f1()
print("Global : ",x)


# In[7]:


'''
Global Scope - 2
'''
x = 10 # Global Scope
def f1():

    def f2():
        global x
        x = 1000
        global y # if y not there then create one in global scope. This option is not there in nonlocal(if var not there then throw error)
        y = 200
        print("In F2 : ",x)
    f2()
    print("In F1 :",x)

f1()
print("Global : ",x,y)


# In[8]:


'''
Builtin Scope

len function not there in 
Local
Enclosed
Global
Then it will go and check in builtins if it is there it will execute else error
'''
s="Hello"
def f1():

    def f2():

        print("In F2 : ",len(s))
    f2()
    print("In F1 :",len(s))

f1()
print("Global : ",len(s))


# In[9]:


print(dir(__builtins__))


# In[10]:


'''
variable my_name is not present in
Local
Enclosed
Global
Builtins
So it throws error after checking in all 4 above
'''

def f1():
    
    def f2():
        
        print("In F2 : ",my_name)
    f2()
    print("In F1 :",my_name)

f1()
print("Global : ",my_name)


# In[ ]:




