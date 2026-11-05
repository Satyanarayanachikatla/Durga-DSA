# chapter-11:-sorting
# ==================
# predefined methods:-
# 1. list.sort()
# 2. sorted(sequence)
# ex:1-sort the elements in a list in ascending order
'''l=[10,14,12,15,13,11]
l.sort()
print(l)
'''
# ex:2-sort the elements in a list in descending order
'''l=[10,14,12,15,13,11]
l.sort(reverse=True)
print(l)
'''
# ex:3-sort the list of names in alphabetical order(asc)
'''l=["HHH","BBB","AAA","ZZZ","aaa","yyy"]
l.sort()
print(l)
'''
# ex-4: sort the names in ascending order based on length of name
'''l=["Ram","Prabash","Charan"]
l.sort()
print(l)
'''
# sort the names in ascending order based on length of name
# stable sort or stable method
'''def fun(s):
    return len(s)
l=["Ram","Prabash","Charan","Car","Cam"]
l.sort(key=fun)
print(l)
'''
'''def fun(s):
    return len(s)
l=["Ram","Prabash","Charan","Car","Cam"]
l.sort(key=fun,reverse=True)
print(l)
'''
# ex:-5. sort the student objects on name
'''class student:
    def __init__(self,name,htno,marks):
        self.name=name
        self.htno=htno
        self.marks=marks
    def __str__(self):
        return f"({self.name},{self.htno},{self.marks})"
def fun(s):
    return s.name
s1=student("prakash",333,90)
s2=student("prasanth",666,50)
s3=student("prabash",222,80)
s4=student("prabhu",111,60)
l=[s1,s2,s3,s4]
print("before sorting")
for i in l:
    print(i)
l.sort(key=fun)
print("after sorting")
for i in l:
    print(i)
'''
# ex-6: sort the students objects based on the htno
'''class student:
    def __init__(self,name,htno,marks):
        self.name=name
        self.htno=htno
        self.marks=marks
    def __str__(self):
        return f"({self.name},{self.htno},{self.marks})"
def fun(s):
    return s.htno
s1=student("prakash",333,90)
s2=student("prasanth",666,50)
s3=student("prabash",222,80)
s4=student("prabhu",111,60)
l=[s1,s2,s3,s4]
print("before sorting")
for i in l:
    print(i)
l.sort(key=fun)
print("after sorting")
for i in l:
    print(i)
'''
# ex-7: sort the student objects based on marks
'''class student:
    def __init__(self,name,htno,marks):
        self.name=name
        self.htno=htno
        self.marks=marks
    def __str__(self):
        return f"({self.name},{self.htno},{self.marks})"
def fun(s):
    return s.marks
s1=student("prakash",333,90)
s2=student("prasanth",666,50)
s3=student("prabash",222,80)
s4=student("prabhu",111,60)
l=[s1,s2,s3,s4]
print("before sorting")
for i in l:
    print(i)
l.sort(key=fun)
print("after sorting")
for i in l:
    print(i)
'''
# ex-8:sort the elements in a list in asc order using absulte method
'''l=[10,-16,13,-11,15]
nl=sorted(l)
print(l)
'''
'''l=[10,-16,13,-11,15]
nl=sorted(l,key=abs)
print(nl)
'''
# bubble sort algorithm:
# ---------------------------
# ex:10-implementing bubble sort algorithm in asc order
'''import random
def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=[]
for i in range(10):
    l.append(random.randint(10,99))                 #randint()=random integer
print(l)
bubblesort(l)
print(l)
'''
# ex-11: implementing bubble sort algorithm in desc order
'''import random
def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=[]
for i in range(10):
    l.append(random.randint(10,99))                 #randint()=random integer
print(l)
bubblesort(l)
print(l)
'''
# ex:12-modified bubble sort if the data is already in sorted order
'''import random
def bubblesort(l):
    for i in range(len(l)-1):
        swaps=False
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],[j]
                swaps=True
        if swaps==False:
            return 
l=[10,20,30,40,50]
bubblesort(l)
print(l)
'''
'''import random
def bubblesort(l):
    c=0
    for i in range(len(l)-1):
        # swaps=False
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                c+=1
                l[j],l[j+1]=l[j+1],[j]
                # swaps=True
        # if swaps==False:
            # return 
            # return 
    return c
l=[10,20,30,40,50]
print(bubblesort(l))
print(l)
'''
# class-42:
# ======
# selection sort:
#-----------------
# ex:-13. implementation of section sort in asc order
'''import random
def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        min_i=i
        for j in range(i+1,n):
            if l[j]<l[min_i]:
                min_i=j
        l[i],l[min_i]=l[min_i],l[i]
l=[]
for i in range(10):
    l.append(random.randint(10,99))
print(l)
selectionsort(l)
print(l)
'''
# ex-14:-implementation of election sort in desc order
'''import random
def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        max_i=i
        for j in range(i+1,n):
            if l[j]>l[max_i]:
                max_i=j
        l[i],l[max_i]=l[max_i],l[i]
l=[]
for i in range(10):
    l.append(random.randint(10,99))
print(l)
selectionsort(l)
print(l)
'''
# insertion sort
# ==========
# ex:15-implementation of insertion sort in asc order
'''import random
def insertionsort(l):
    n=len(l)
    for i in range(1,n):
        x=l[i]
        y=i-1
        while y>=0 and x<l[y]:
            l[y+1]=l[y]
            y=y-1
        l[y+1]=x
l=[]
for i in range(10):
    l.append(random.randint(10,99))
print(l)
insertionsort(l)
print(l)
'''
# ex:16-implementation of insertion sort in desc order
''''import random
def insertionsort(l):
    n=len(l)
    for i in range(1,n):
        x=l[i]
        y=i-1
        while y>=0 and x>l[y]:
            l[y+1]=l[y]
            y=y-1
        l[y+1]=x
l=[]
for i in range(10):
    l.append(random.randint(10,99))
print(l)
insertionsort(l)
print(l)
'''
# class-43
# ======
