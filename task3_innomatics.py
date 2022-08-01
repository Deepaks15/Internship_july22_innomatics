#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cmath import *

z = input()

print(abs(complex(z)))
print(phase(complex(z)))


# In[ ]:


import math
xy=int(input())
yz=int(input())
zx=math.hypot(xy,yz)
mz=zx/2
yzx=math.xsin(1*xy/zx)
ym=math.sqrt((yz**2+mz**2)-(2*yz*mz*math.cos(yzx)))
myz=math.xsin(math.sin(yzx)*mz/ym)
print(int(round(math.degrees(myz),0)),'\u00B0',sep='')


# In[ ]:


for i in range(1,int(input())+1):
    print (((10**i - 1)//9)**2)


# In[ ]:


print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))


# In[ ]:


a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')


# In[ ]:


#IntegersComeInAllSizes
a,b,c,d = (int(input()) for _ in range(4))
print (pow(a,b)+pow(c,d))


# In[ ]:



#TriangleQuest
for i in range(1,int(input())): 
    print((10**(i)//9)*i)


