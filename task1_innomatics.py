#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "Hello, World!"
print(a)


# In[2]:


k = int(input())
if k%2 == 1:
    print("Weird")
elif k%2 ==0 and 2<= k <=5:
    print("Not Weird")
elif k%2 ==0 and 6<=k <=20:
    print("Weird")
else:
    print("Not Weird") 


# In[3]:


m = 3
n = 2
print(m+n)
print(m-n)
print(m*n)


# In[4]:


x=4
y=3
print(x//y)
print(x/y)


# In[5]:


a = int(input())
for i in range(0,a):
 print(i*i)


# In[6]:


def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    
    
    return leap


# In[7]:


year = int(input())
print(is_leap(year))


# In[10]:


if __name__ == '__main__':
  n = int(input())
  for i in range (1,n+1):
      print(i,end='')


# In[ ]:




