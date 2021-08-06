#!/usr/bin/env python
# coding: utf-8

# In[26]:


f = open("numbers1.txt", 'r')
s = f.readlines()
p = str(s)

total = 0

for line in s:
    
    printnum = 0
    try: 
        printnum += int(line)
        total += printnum
        
    except ValueError:
        print("Invalid Literal for Int():", ValueError)

print(total)

