#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sayeed Khan - 6 Dec-2021
#sum of digits
n=int(input("Enter a number:"))
total=0
while(n>0):
    dig=n%10
    total=total+dig
    n=n//10
print("The total sum of digits is:",total)


# In[ ]:




