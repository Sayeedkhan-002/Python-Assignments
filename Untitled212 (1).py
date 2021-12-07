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


# In[2]:


#Sayeed Khan - 6 Dec-2021
#Reverse of a number
number = int(input("Enter the integer number: "))   
revs_number = 0        
while (number > 0):  
   
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
  
 
print("The reverse number is : {}".format(revs_number))  


# In[ ]:




