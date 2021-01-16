#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Object Oriented Programming
'''


# In[2]:


'''
Using Procedural Programming
Example: Personal Loan
'''

employee_name = "abc"

month_1_salary = 20000
month_1_tax = 2000
month_1_rent = 10000

month_2_salary = 22000
month_2_tax = 2200
month_2_rent = 10000


print("employee_name : ",employee_name)

print("month_1_salary : ",month_1_salary)
print("month_1_tax : ",month_1_tax)
print("month_1_rent : ",month_1_rent)

print("month_2_salary : ",month_2_salary)
print("month_2_tax : ",month_2_tax)
print("month_2_rent : ",month_2_rent)


# In[5]:


'''
Using Object Oriented Approch -- Finally we are writing code inside the class
'''

class Employee:
    name = "abc"

class month1:
    salary = 20000
    tax = 2000
    rent = 10000

class month2:
    salary = 22000
    tax = 2200
    rent = 10000

print(dir(Employee))
print("-"*40)
print(dir(month1))
print("-"*40)
print(dir(month2))

#print(locals())    
    
print("employee_name : ",Employee.name)

print("month_1_salary : ",month1.salary)
print("month_1_tax : ",month1.tax)
print("month_1_rent : ",month1.rent)

print("month_2_salary : ",month2.salary)
print("month_2_tax : ",month2.tax)
print("month_2_rent : ",month2.rent)

# Advantages
# 1) We were able to organise - Encapsulation
# 


# In[ ]:




