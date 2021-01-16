#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

def squares(M):
    for i in M:
        time.sleep(0.1)
        print("Square : ",i*i)

def cubes(M):
    for i in M:
        time.sleep(0.1)
        print("cube : ",i*i*i)


if __name__ == "__main__":
    L = range(100) # range function will generate numbers 0 to 5

    from multiprocessing import Process

    p1 = Process(target=squares,args=(L,))
    p2 = Process(target=cubes,args=(L,))
    st = time.time()
    p1.start() # It will start and IT WILL NOT WAIT FOR THREAD to complete
    p2.start()
    p1.join()
    p2.join()
    et = time.time()
    print("Total time in threads : ",et-st)


# In[ ]:




