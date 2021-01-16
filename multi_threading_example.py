#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
Multi Threading : 1 Process -> multiple pieces (threads) --> run parallelly
1. Make use of processor more
2. Increase the execution speed.

BUT

In python, Multithreading is NOT PARALLEL
In Interpreter, we have lock implemented called as GIL (GLOBAL INTERPRETER LOCK)
GIL : It allows one bytecode to run at a time

Python code --> Bytecode --> Bytecode wiil convert into m/c readable code and execute

'''

'''
Still we can make use of multithreading

Assume that some threads are interactiong with DB/network resource/io stream WHERE it cause delay in getting the data
During that delay, interpreter will execute other threads
'''

'''
Multi Threading : 1 Process -> multiple pieces (threads) --> run parallelly
Multiprocessing : multiple processes --> each run parallely
'''


# In[7]:


import time

def squares(M):
    for i in M:
        time.sleep(0.1)
        print("Square : ",i*i)

def cubes(M):
    for i in M:
        time.sleep(0.1)
        print("cube : ",i*i*i)

L = range(5) # range function will generate numbers 0 to 5
st = time.time()
squares(L)
cubes(L)
et = time.time()
print("total time : ",et-st)


# In[8]:


import time

def squares(M):
    for i in M:

        print("Square : ",i*i)

def cubes(M):
    for i in M:
        
        print("cube : ",i*i*i)

L = range(5) # range function will generate numbers 0 to 5

from threading import Thread

t1 = Thread(target=squares,args=(L,))
t2 = Thread(target=cubes,args=(L,))

t1.start() # It will start and IT WILL NOT WAIT FOR THREAD to complete
t2.start()


# In[9]:


import time

def squares(M):
    for i in M:
        time.sleep(0.1)
        print("Square : ",i*i)

def cubes(M):
    for i in M:
        time.sleep(0.1)
        print("cube : ",i*i*i)

L = range(5) # range function will generate numbers 0 to 5

from threading import Thread

t1 = Thread(target=squares,args=(L,))
t2 = Thread(target=cubes,args=(L,))
st = time.time()
t1.start() # It will start and IT WILL NOT WAIT FOR THREAD to complete
t2.start()
t1.join()
t2.join()
et = time.time()
print("Total time in threads : ",et-st)


# In[ ]:




