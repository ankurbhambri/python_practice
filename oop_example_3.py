#!/usr/bin/env python
# coding: utf-8

# In[4]:


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

month_3_salary = 22000
month_3_tax = 2200
month_3_rent = 10000

month_4_salary = 22000
month_4_tax = 2200
month_4_rent = 10000


print("employee_name : ",employee_name)

print("month_1_salary : ",month_1_salary)
print("month_1_tax : ",month_1_tax)
print("month_1_rent : ",month_1_rent)

print("month_2_salary : ",month_2_salary)
print("month_2_tax : ",month_2_tax)
print("month_2_rent : ",month_2_rent)

print("month_3_salary : ",month_3_salary)
print("month_3_tax : ",month_3_tax)
print("month_3_rent : ",month_3_rent)

print("month_4_salary : ",month_4_salary)
print("month_4_tax : ",month_4_tax)
print("month_4_rent : ",month_4_rent)


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

class month3:
    salary = 22000
    tax = 2200
    rent = 10000

class month4:
    salary = 22000
    tax = 2200
    rent = 10000
    
    
print("employee_name : ",Employee.name)

print("month_1_salary : ",month1.salary)
print("month_1_tax : ",month1.tax)
print("month_1_rent : ",month1.rent)

print("month_2_salary : ",month2.salary)
print("month_2_tax : ",month2.tax)
print("month_2_rent : ",month2.rent)

print("month_3_salary : ",month3.salary)
print("month_3_tax : ",month3.tax)
print("month_3_rent : ",month3.rent)

print("month_4_salary : ",month4.salary)
print("month_4_tax : ",month4.tax)
print("month_4_rent : ",month4.rent)


# If we want to store 20 months data then we need to create 20 classes. But there is a solution for resusing the code


# In[6]:


'''
# If we want to store 20 months data then NOT REQUIRED TO CREATE 20 more classes. We have other option

class help us to create Multiple objects
'''

class Employee:
    name = "abc"

class Month:
    def __init__(self,s,t,r):
        self.salary = s
        self.tax = t
        self.rent = r

# Instead of creating 20 more classes, define the generic class and OBTAIN copy (also called as creating OBJECT)

# Point-1  : Super class for all the class is object class

# Point-2 : Calling class name will create object 
# Example : month1 = Month(20000,2000,10000)

# Point-3 : To create object it calls 2 methods internally
# 1. __new__ # This method will construct/build/create new object
# 2. __init__ # This method will initialize the object

# Point-4 : 
# month1 = Month(20000,2000,10000)
# __init__(month1,20000,2000,10000)  # self - month1

# month2 = Month(22000,2200,10000)
# __init__(month2,22000,2200,10000) # self - month2

# Terminology
# month1,month2-4 are INSTANCE OBJECTS
# Employee - CLASS OBJECT
# salray,tax,rent are INSTANCE VARIABLES
# name inside employee class - called as CLASS VARIABLE


month1 = Month(20000,2000,10000)
month2 = Month(22000,2200,10000)
month3 = Month(22000,2200,10000)
month4 = Month(22000,2200,10000)

print("employee_name : ",Employee.name)

print("month_1_salary : ",month1.salary)
print("month_1_tax : ",month1.tax)
print("month_1_rent : ",month1.rent)

print("month_2_salary : ",month2.salary)
print("month_2_tax : ",month2.tax)
print("month_2_rent : ",month2.rent)

print("month_3_salary : ",month3.salary)
print("month_3_tax : ",month3.tax)
print("month_3_rent : ",month3.rent)

print("month_4_salary : ",month4.salary)
print("month_4_tax : ",month4.tax)
print("month_4_rent : ",month4.rent)

