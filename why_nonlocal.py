#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Track total accounts avaiable using GLOBAL VARIABLE
'''
total_count = 0

def create_account():
    global total_count
    total_count = total_count + 1 # total_count += 1

def delete_account():
    global total_count
    total_count = total_count - 1 # total_count -= 1


create_account()
create_account()
create_account()
create_account()

total_count = 100

delete_account()

print("Total Account avaialble : ",total_count)


# In[3]:


'''
Design a function in such a way that we can make use of enclosed scope varaible
'''

def main_account():
    count=0

    def CA():
        nonlocal count
        count += 1
    
    def DA():
        nonlocal count
        count -= 1
    
    def Total():
        return count # Since we are reading, not required to mentions nonlocal

    #CA() #point-1
    #DA() #point-2
    #Total() #point-3
    
#main_account() # #point-4

# point 1- 4 WON work

# CA() # We can' access outside
# CA() # We can' access outside

# DA() # We can' access outside


# In[5]:


'''
Since we need to access all 3 functions outside, we can also return FUNCTION objects like other objects
'''

def main_account():
    count=0

    def CA():
        nonlocal count
        count += 1
    
    def DA():
        nonlocal count
        count -= 1
    
    def Total():
        return count # Since we are reading, not required to mentions nonlocal

    return (CA,DA,Total) # We are not calling each func like CA(), instead we are returning function object CA


result = main_account()
#result = (CA,DA,Total)



# call create account
result[0]()

# call create account
result[0]()

# call create account
result[0]()

# call create account
result[0]()

count=100 # It will create global variable, No access to variable inside the function

# call delete account
result[1]()


# Get total count
tc = result[2]()
print("Total Accounts : ",tc)




# In[ ]:




