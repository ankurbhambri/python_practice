#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Using Procedural Programming
Example: Personal Loan

view RBI rules--> we have seperate class that we need to make use

'''

employee_name = "abc"

rate_of_interest = 10

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

phone_bill = 500

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

print("rate_of_interest : ",rate_of_interest)

def avg_salary(s1,s2,s3,s4):
    return (s1+s2+s3+s4)/4

a = avg_salary(month_1_salary,month_2_salary,month_3_salary,month_4_salary)
print("avg salary : ",a)

print("phone_bill : ",phone_bill)

class RBI:
    def view_rules(self):
        return "RBI Rules"

a= RBI()

print("RBI Rules : ",a.view_rules())


# In[3]:


'''
Add method to compute avg salary
'''

class Month:
    
        
    name = "abc"
    
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
    
    #def add_rate_of_interest(self,i): # On each INSTANCE object rate_of_interes will get stored. which is not required
    #    self.rate_of_interest = i 
    
    @classmethod
    def add_rate_of_interest(cls,i):
        cls.rate_of_interest = i
    
    @staticmethod
    def avg_salary(s1,s2,s3,s4):    
        return (s1+s2+s3+s4)/4

# Inheritance --


class New_Month(Month):
    def add_phone_bill(self,b):
        self.phone_bill =b
        
    def view_phone_bill(self):
        return self.phone_bill

    
class RBI:
    def view_rules(self):
        return "RBI Rules"

class Brand_New_Month(New_Month,RBI):
    pass

month1 = Brand_New_Month()
month2 = Brand_New_Month()
month3 = Brand_New_Month()
month4 = Brand_New_Month()


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

print("employee_name : ",Brand_New_Month.name)

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

Brand_New_Month.add_rate_of_interest(10)
print("rate_of_interest : ",Brand_New_Month.rate_of_interest)

month1.add_phone_bill(250)
print("phone_bill : ",month1.view_phone_bill())

print("RBI Rules : ",month1.view_rules())


# In[ ]:




