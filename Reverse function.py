#!/usr/bin/env python
# coding: utf-8

# In[5]:


def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str
    
s = "1234abcd"
print("The original string:",end='')
print(s)
print("The reverse string:",end='')
print(reverse(s))
   

