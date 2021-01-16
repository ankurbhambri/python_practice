#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("stmt-1")
print("stmt-1")
print("stmt-1")
print("stmt-1")
print(x) # Error - Program ternaminate here
print("stmt-1")
print("stmt-1")
print("stmt-1")
print("stmt-1")
print("stmt-1")
print("stmt-1")
print("stmt-1")


# In[4]:


try:
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print(x) # Error - Control will go to except block
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
except:
    print("In Except")
print("stm-2")
print("stm-2")
print("stm-2")
print("stm-2")
print("stm-2")


# In[8]:


a = 10
#b = 0
try:
    result = a/b
    print("result : ",result)
except :
    print ("In except")


# In[4]:


'''
1. All exception we have  classes, if not there we can write our own
2. Super class for all exception classes : Exception
3. try clearly know which exception occurred
4. In except block, we can write Exception class name
'''
c = 10
#d = 0
L=[]
D={}
try:
    F=open("ajksdjaskdjkl.txt","r")
    print(D["name"])
    print(L[10]) # 10th index
    result = c/d
    print("result : ",result)
except ZeroDivisionError:
    print("It is ZDE")
except NameError as ne:
    print("It is NE and captured object is : ",ne)
except (KeyError,IndexError):
    print("It is either KE or IE")
except:
    print("Some Error")
print("Outside statements")


# In[2]:


'''
try-except-else
'''
e=10
f=0

try:
    r = e/f
    print("r: ",r)

except: # If try Block Failed
    print("In Except")
    try:
        print(name)
    except:
        print("Inside try")
    
else: # If try Block Success
    r2 = e/e
    print("r2 : ",r2)
    print("In Else")

print("Some other statements")

    


# In[7]:


'''
try-finally
try-except-finally
try-except-else-finally
'''
g = 10
h = 0
try:
    r = g/h
    print("r : ",r)
except:
    try:
        print("course : ",course)
    except NameError as ne:
        print("It is name error ",ne)
    #print("In Except")
finally:
    print("In Finally")

print("Some Other Statements")


# In[11]:


'''
raise
'''
i=10
j=10
try:
    if j == 0:
        raise ZeroDivisionError("J is 0") # raise also used to throw custom exceptions
        
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-1")
    print("stmt-100")
    r = i/j
    print("r : ",r)
except:
    print("From raise")

print("Outside statements")


# In[13]:


'''
assert statment
assert some_condition,"Some message"
condtion True means, It will not do anything, it will proceed to next line
If condition False then it will throw exception called "AssertionError"
'''
result = "test case -10 success"

try:
    assert "success" in result, "Some test failed"
    print("other statements inside the try block")
except AssertionError as ae:
    print("ae : ",ae)

print("outside statements..")


# In[16]:


'''
Super class will be able handle subclass exception

class MyClass(Exception):
    pass

class MyClass(ZeroDivisionError):
    pass

try:
  pass
except MyClass:  # OR except ZeroDivisionError # Here if myclass execption comes then ZDE class will be able to handle
   pass
   
To Summarize : Super class will be able to handle subclass exception
'''

try:
    L=[]
    #print(x)
    #print(L[10])
    F=open("asdskdl.txt","r")
except Exception as e:
    print("e is : ",e)
    print("type(e) is : ",type(e))
    print("type(e).__name__ is : ",type(e).__name__)
          


# In[19]:


'''
Custom Classes
if we want to create a custom exception class then condition is , our class should be subclass of Exception class
'''
class MyError(Exception):
    pass

x = 10
y = 0

try:
    if y == 0:
        raise MyError("Y is 0, so got this error")
    r = x/y
    print("r : ",r)
except MyError as me:
    print("me : ",me)


# In[20]:


'''
Custom Classes
if we want to create a custom exception class then condition is , our class should be subclass of Exception class
'''
class MyError(Exception):
    pass

x = 10
y = 0

try:
    if y == 0:
        raise MyError("Y is 0, so got this error")
    r = x/y
    print("r : ",r)
except Exception as me:
    print("me : ",me)


# In[22]:


class MyError(Exception):
    def __init__(self,m):
        self.msg =m

    def __str__(self):
        return "Error Details : " + self.msg

x = 10
y = 0

try:
    if y == 0:
        raise MyError("Y is 0, so got this error")
    r = x/y
    print("r : ",r)
except MyError as me:
    print("me : ",me)


# In[ ]:




