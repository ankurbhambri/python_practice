#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[4]:


'''
We dont have data at the time of object creation, we need to add dynamically data to object

setter/getter
'''


class Employee:
    name = "abc"

class Month:
    
    def add_salary(self,s):
        self.salary = s
    
    def add_tax(self,t):
        self.tax = t
    
    def add_rent(self,r):    
        self.rent = r
    
    def view_salary(self):
        return self.salary
    
    def view_tax(self):
        return self.tax
    
    def view_rent(self):
        return self.rent


month1 = Month()
month2 = Month()
month3 = Month()
month4 = Month()


month1.add_salary(20000)
month1.add_tax(2000)
month1.add_rent(10000)

month2.add_salary(22000)
month2.add_tax(2200)
month2.add_rent(10000)

month3.add_salary(22000)
month3.add_tax(2200)
month3.add_rent(10000)

month4.add_salary(22000)
month4.add_tax(2200)
month4.add_rent(10000)

print("employee_name : ",Employee.name)

print("month_1_salary : ",month1.view_salary())
print("month_1_tax : ",month1.view_tax())
print("month_1_rent : ",month1.view_rent())

print("month_2_salary : ",month2.view_salary())
print("month_2_tax : ",month2.view_tax())
print("month_2_rent : ",month2.view_rent())

print("month_3_salary : ",month3.view_salary())
print("month_3_tax : ",month3.view_tax())
print("month_3_rent : ",month3.view_rent())

print("month_4_salary : ",month4.view_salary())
print("month_4_tax : ",month4.view_tax())
print("month_4_rent : ",month4.view_rent())

