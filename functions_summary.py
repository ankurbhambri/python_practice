#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add():
    pass

def add(a,b):
    pass

def add(a,b=10):
    pass

#def add(a=10,b): # WRONG
#    pass

def add(b,a=10): # CORRECT
    pass

def add(*a): # takes only 0 or more POSITIONAL args
    pass

def add(**a): #takes only 0 or more Keyword only args
    pass

def add(*a,**b): # takes only 0 or more POSITIONAL args AND takes only 0 or more Keyword only args
    pass

def add(a,b,*,c,d): # a,b are positional AND c and d are keywrod only
    pass


def add(*,a,b): # a and b both are KEYWORD Only
    pass

