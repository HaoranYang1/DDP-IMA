#!/usr/bin/env python
# coding: utf-8

# In[1]:


def unique_letters(s):
    string =''
    for str in s:
        if str not in string:
            string += str
    lst = list(string)
    nl = []
    for i in lst:
        if i.isalpha():
            s = i.upper()
            nl.append(s)
    n = len(nl)
    print(nl, n)

unique_letters("Hello World")






