#!/usr/bin/env python
# coding: utf-8

# In[2]:



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    output = [];
    xyz = [];
    for A in range (a+1):
        for B in range (b+1):
            for C in range (c+1):
                if A+B+C != d:
                    xyz = [A,B,C];
                    output.append(xyz);
print(output);  



# In[ ]:


if __name__ == '__main__':
    k = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])


# In[ ]:


if __name__ == '__main__':
    students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    x = 99999
    for i in range (len(students)):
        if x>float(students[i][1]):
            x = float(students[i][1])
    y = 999999   
    for i in range(len(students)):
        if float(students[i][1])>float(x) and y > float(students[i][1]):
            y = float(students[i][1])
    runner = []
    for i in range(len(students)):
        if float(students[i][1]) ==float(y):
            runner.append(students[i][0])
    runner = sorted(runner)
    for i in range(len(runner)):
        print(runner[i])   


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    output = list(student_marks[query_name])
    per = sum(output)/len(output);
    print("%.2f" % per);


# In[ ]:


if __name__ == '__main__':
    N = int(input())
    L=[];
    for i in range(0,N):
        cmd=input().split();
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop();
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort();
        else:
            L.reverse();


# In[ ]:


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))
    


# In[ ]:


from __future__ import division

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':


# In[ ]:


if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for i in arr:
        if i in good:
            happiness += 1
        elif i in bad:
            happiness -= 1
    print(happiness)


# In[ ]:


A = int(input())
aset = set(map(int, input().split()))
B = int(input())
bset = set(map(int, input().split()))

adef = aset.difference(bset)
bdef = bset.difference(aset)

output = adef.union(bdef)

for i in sorted(list(output)):
    print(i)


# In[ ]:


a = set()
[a.add(input()) for _ in range(int(input()))]
print(len(a))


# In[ ]:


num = int(input())
data = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    data.remove(int(oper[1]))
  elif oper[0] == "discard":
    data.discard(int(oper[1]))
  else:
    data.pop()
    

