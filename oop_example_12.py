#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Abstract Classes
'''

class Employee:
    def add_name(self,n):
        self.name = n
    def view_name(self):
        pass

e = Employee()

    


# In[3]:


'''
HOW TO CREATE abstract class
'''

from abc import ABC,abstractmethod

class Employee(ABC): # Step-1
    def add_name(self,n):
        self.name = n
    @abstractmethod #  Step-2
    def view_name(self):
        pass
    
e = Employee()


# In[5]:


'''
How to make use of abstract class
'''

from abc import ABC,abstractmethod

class Employee(ABC): # Step-1
    def add_name(self,n):
        self.name = n
    @abstractmethod #  Step-2
    def view_name(self):
        pass
    
class New_Employee(Employee):
    def view_name(self):
        return "Hello " + self.name

    

e = New_Employee()
e.add_name("Some Name")
print(e.view_name())


# In[ ]:




