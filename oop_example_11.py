#!/usr/bin/env python
# coding: utf-8

# In[17]:


'''
Operator Overloading
'''

class Employee:
    def __init__(self,n):
        self.ename = n
        
    def __add__(self,x): #__add__(e1,e2) # self->e1, x-> e2
        return self.ename + x.ename
    
    def __str__(self): # __str__(e1)
        return self.ename
    
    def __len__(self):
        return len(self.ename)
    
    def __iter__(self): # This will be called ONE time # we can use it for initialisation
        self.current_index =0
        return self
    
    def __next__(self): # This will be called in each iteration. # We can use to return value for each iteration
        if self.current_index < len(self.ename):
            c = self.current_index
            self.current_index = self.current_index + 1
            return self.ename[c]
        else:
            raise StopIteration
            
    
        
e1 = Employee("abc")
e2 = Employee("xyz")



# + --> __add__

result = e1 + e2 # e1.__add__(e2) # __add__(e1,e2)

print("result : ",result)

s = "Python"
print("s : ",s)

print("e1 : ",e1)


print("Length of s : ",len(s))
print("Length of e1 : ",len(e1))

for i in s:
    print("i : ",i)

for j in e1:
    print("j : ",j)


# In[ ]:





# In[ ]:




