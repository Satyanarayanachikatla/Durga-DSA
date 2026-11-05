# chapter-04:- Data Structures in python
# ===========================
# 1.mutable objects(changeble):- list,set,dict
# 2.immutable objects(un-changeble):- tuple,string and fundamental datatypes(int,float,complex,bool,string,None)
# string data structure:
# ------------------------
# s1='hai'
# s2="hai"
# s3="""hai"""
# s4='''hai'''
# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(type(s4))
# Accesing string objects
# --------------------------
# while loop:
'''s="hai"
i1=0
while i1<len(s):
    print(f"+ve index={i1} and it value={s[i1]}")
    i1=i1+1
'''
'''s="hai"
i1=0
i2=-len(s)
while i1<len(s):
    print(f"+ve index={i1} and it value={s[i1]} and -ve index {i2} value={s[i2]}")
    i1+=1
    i2+=1
'''
# class-20
# ---------
# slice operator
# syntax:-[satrt:stop:step]
'''s="abcdefg"
print(s[0])
print(s[6])
print(s[0:7:1])
print(s[::])
print(s[-1:-8:-1])
print(s[-3:-6:-1])
print(s[-1:-8:])
print(s[::-1])
# note: slicing method never generate error message
'''
# operators on string objects
'''s1="abc"
s2="def"
print(s1+s2)
'''
'''s1="abc"
s2=10
print(s1+str(s2))
print(s1+s2) #error
'''
'''s1="ab"
s2=2
print(s1*s2)
'''
'''s1="ab"
s2="3"
print(s1*s2) #error
'''
'''s1="ab"
s2="3"
print(s1*int(s2))
'''
'''s="satya"
print('a' in s)
print('b' in s)
print('a' not in s)
print('b' not in s) 
'''
'''print("mno"<"xyz")
print("abc"<"myz")
print("mno"<"mno")
print("mno"<="mno")
'''
# common function:
'''s="prakash"
print(s)
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))
print(sorted(s,reverse=True))
print(ord('a'))
print(ord('A'))
print(ord('o'))
print(chr(97))
print(chr(48))
'''
# class-21
# -----------
# string specific functions
'''s="welcome to PYTHON PROGRAMMING"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())
'''
'''s="abcdabcaba"
print(s.count('a'))
print(s.count("e"))
print(s.count("b"))
'''
# replace(old,new)
'''s="abcdabcaba"
print(s.replace('a','b'))
print(s.replace("ab","x"))
'''
# startswith(),endswith()
'''s="python is easy"
print(s.startswith("java"))
print(s.startswith("python"))
print(s.startswith("pyja"))

print(s.endswith("difficult"))
print(s.endswith("easy"))
'''
# index(substring),find(sunstring)
'''s="python is easy"
print(s.index("is"))
print(s.index("was"))  #error
print(s.find("is"))
print(s.find("was"))
'''
# split(delimiter)
'''s="python is easy"
print(s.split(" "))

s="24/09/2025"
print(s.split("/"))

s="13:26:30"
print(s.split(":"))
'''
# seperator.join(list)
'''l=["python","is","easy"]
print(" ".join(l))
print(":".join(l))

l="python is easy"
print(' '.join(l))
'''
# isalnum()
'''print("1".isalnum())
print("a".isalnum())
print("#".isalnum())
'''
# isalpha()
'''print("1".isalpha())
print("a".isalpha())
'''
# isdigit()
'''print("1".isdigit())
print("a".isdigit())
'''
# islower()
'''print('a'.islower())
print("a".islower())
print("A".islower())
'''
# isupper()
'''print("a".isupper())
print("A".isupper())
'''
# isspace()
'''print("".isspace())
print(" ".isspace())
'''
'''def removedigit(s):
    l=list(s)
    l1=[]
    for i in s:
        if not  i.isdigit():
            l1.append(i)
    return "".join(l1)
s=input("enter a string:")
print(removedigit(s))
'''
# class-22
# ---------
# list data structure
'''l=[10,10.34,"abc",True,"i+2j"]
print(l)
print(type(l))
'''
# creation of list objects
# [ ], [obj1,obj2,...], list(), split(), input() with list(), eval ()
# slicing
'''l=[10,20,30,40]
print(l[0:len(l)])
print(l[::])
'''
# while loop
'''l=[10,20,30,40]
index=0
while index<len(l):
    print(l[index])
    index+=1
'''
# for each loop
'''l=[10,20,30,40]
for i in l:
    print(i)
'''
# nested list objects
'''l=[100,200,[111,222,333],30,400,500]
print(l[0])
print(l[2])
print(l[2][0])
'''
# list aliasing
'''l1=[1,2,3,4,5]
l2=l1
print(l1 is l2)
l1[2]=999
print(l1)
print(l2)
'''
'''p=print
p("welcome")
'''
# shallow copy
# deep copy

# list cloning
# --------------
'''l1=[1,2,3,4,5]
l2=l1.copy()
print(l1)
print(l2)
print(l1 is l2)
print(l1==l2)

l1[2]=888
print(l1)
print(l2)
print(l1==l2)
'''
# special case in cloning with respective to nested list
# case-1
'''l1=[11,22,33,[111,222,333],44,55]
l2=l1.copy()
print(l1)
print(l2)
l1[1]=888
print(l1)
print(l2)
'''
# case-2
'''l1=[11,22,33,[111,222,333],44,55]
l2=l1.copy()
print(l1)
print(l2)
l1[3][1]=999
print(l1)
print(l2)
'''
# class-23
# ---------
# shallow copy or normal copy
# -----------------------------------
'''l1=[1,2,[1,2],55]
l2=l1.copy()
print(l1)
print(l2)
l1[2][1]=999
print(l1)
print(l2)
'''
'''import copy
l1=[11,22,[111,222],55]
l2=copy.copy(l1)   #shallow copy
l1[2][1]=999
print(l1)
print(l2)
print(l1 is l2)
print(l1[2] is l2[2])
'''
# Deep copy
'''import copy
l1=[1,22,33,[111,222,333],44,55]
l2=copy.deepcopy(l1)   #Deep copy
print(l1)
print(l2)
l1[3][1]=666
print(l1)
print(l2)
'''
# list comprehension
# 1.increment each element present in a list
'''ol=[1,2,3,4,5]
nl=[i+1 for i in ol]
print(ol)
print(nl)
'''
# 2.find factorial of each element present in a list
'''import math
ol=[1,2,3,4,5]
nl=[math.factorial(i) for i in ol]
print(ol)
print(nl)
'''
# 3.convert every name present in list into upper case
'''ol=["prakash","raju","ram","jamu"]
nl=[i.upper() for i in ol]
print(ol)
print(nl)
'''
# exact even number in a list
'''ol=[1,2,3,4,5,6,7,8,9]
nl=[i for i in ol if i%2==0]
print(ol)
print(nl)
'''
'''ol=[1,2,3,4,5,6]
nl=[i if i%2==0 else "*" for i in ol ]
print(ol)
print(nl)
'''

# common function on list
'''l=[1,2,3,4,5,6]
print(l)
print(len(l))  #len()
print(max(l))   #max()
print(min(l))    #len()
print(sorted(l))   #sorted()
print(sorted(l,reverse=True))  #sorted(variable,reverse=True)
'''
# class-24
# ---------
# list specific methods
'''l=[1,2,3,4]
l.append(5)   #append(object)
print(l)

l.insert(0,9)   #insert(index_value,object)
print(l)

l.remove(9)    #remove(object)
print(l)

l.pop(0)         #pop(index_value)
print(l)

l.clear()         #clear()
print(l)
'''
'''l=[10,20]
print(l.index(20))  #index(object)

print(l.count(10))   #count(object)

l.reverse()               #reverse()
print(l)    

l.sort()   #sort()
print(l)

l.sort(reverse=True)    #sort(reverse=True)
print(l)
'''
# Tuple Data Structure --->immutable object(un-changble)
# ==============
'''T=()
print(T)
print(type(T))
'''
'''t=(1,2)
print(t)
print(type(t))
'''
'''t=(1)
print(t)
print(type(t))    #int
'''
'''t=(1,)
print(t)
print(type(t))      #tuple
'''
'''t=("hello")
print(t)
print(type(t))    #string
'''
'''t=("hello",)
print(t)
print(type(t))     #tuple
'''
# creation of tuple objcets:
# ---------------------------
# 1.()  ,  (obj1,obj2,...),   (obj,),    tuple(),  input() with tuple(),   eval()
'''t=tuple([10,20,30])
print(t,type(t))
'''
'''t=tuple("hello")
print(t,type(t))
'''
'''t=tuple(input("enter a values"))
print(t)
'''
'''t=eval(input("enter tuple:"))
print(t,type(t))
'''
# accseing Tuple objects:
# -------------------------
# 1. directly, index concept, slice operator, while loop, for each loop
'''t=(10,20,30,40,50)
print(t[1:4])
print(t[1:4:1])
print(t[1:4:2])
'''
# nested Tuple objects:
# -------------------------
'''t=(1,2,(3,4),5)
print(t)
print(type(t))
'''
# Tuple cloning:--- it is not allowed
'''t1=(1,2,3)
t2=t1
print(t1)
print(t2)
print(type(t2))
'''
'''import copy
t1=(1,2,3)
t2=t1.copy()
print(t2)        #AttributeError: 'tuple' object has no attribute 'copy'
'''
# tuple comprehension
# ---------------------------
'''t1=(1,2,3,4)
t2=tuple(i+1 for i in t1)
print(t2)
'''
# common functions on tuple
# ------------------------------
'''t=(1,2,3)
print(len(t))             #len()
print(max(t))        #max()
print(min(t))       #min()
print(sorted(t))    #sorted()
print(sorted(t,reverse=True))       #sorted(object,reverse=True)
print(sum(t))          #sum()
'''
# Tuple specific methods
# ---------------------------
'''t=(1,2,3)
print(t.index(2))   #variable.index(object)
print(t.count(2))   #variable.count(object)
'''
# tuple packing and unpacking
# --------------------------------
# unpacking: converting Tuple into individual objects
# packing: converting indidual objects into Tuple
'''a=111
b=222
c=333
t=a,b,c    #tuple Packing
print(a,type(a))     #111 <class 'int'>
print(t,type(t))         #(111, 222, 333) <class 'tuple'>
'''
'''t=(999,888,777,666)
w,x,y,z=t        #Tuple un packing
print(w,type(w))      # 999 <class 'int'>
print(t,type(t))          # (999, 888, 777, 666) <class 'tuple'>
'''
# Set Data Structure--(mutable objects)
# ================
'''s={1,2,3,4,5}
print(s)
for i in s:
    print(i)
'''
'''s={1}
print(s,type(s))
'''
'''s={}
print(s,type(s))   #dict
'''
# creation of set objects
# -------------------------
# 1. set(), {obj1,obj2,obj3,...}, input() with set(), eval()

# acessing set objects
# ----------------------
# ḍirectly,for each loop

# common function on set
# ---------------------------
'''s={1,2,3,4,5}
print(len(s))             #len()
print(max(s))           #max()
print(min(s))           #min()
print(sorted(s))          #sorted()
print(sorted(s,reverse=True))    #sorted(s,reversr=True)
'''
# set specific methods
# ------------------------
'''s={1,2,3,4,5}
s.add(40)    #add()
print(s)
s.remove(40)
# s.remove(100)      #error 
print(s)
s.discard(100)
print(s)
'''
# union,intersection,difference
# --------------------------------
'''heros={"chiru","bala","PSPK","venky"}
poli={"cbn","kcr","bala","PSPK"}
print(heros.union(poli))
print(heros.intersection(poli))
print(heros.difference(poli))
print(poli.difference(heros))
print(heros.symmetric_difference(poli))
'''
# class-25
# ========
# Dictionary data structure--Mutable
# =====================
# collection of individual objects:str,list,tuple,set
'''d = {
    "name": "Satya",          # str
    "marks": [80, 90, 85],    # list
    "address": ("AP", "India"), # tuple
    "subjects": {"Python", "Java"} # set
}
print(d)
'''
'''d={1:"one",2:"two",3:"three"}
print(d)
'''
'''d={1:"one",2:"two"}
d[2]="aaa"
print(d)
'''
# Dict methods
# ===========
'''d={"prakash":[10,20,30]}
print(d)
d={[10,20,30]:"prakash"}
print(d)                         #error
'''
# key must bu immutable objcets
'''d={1:"one"}
d[2]="two"                #add
print(d)
del d[2]                #delete
print(d)
d.clear()             #clear()
print(d)
'''
'''d={1:"one",2:"two"}
print(d.keys())             #keys()
print(d.values())          #values()
print(d.items())          #items()
print(d.get(1))            #get(key)
print(d.get(3))
print(d.get(2,"NA"))     #get(key,default)
print(d.get(3,"Na"))
'''
# dictionary comprehension
# ----------------------------
# syntax:-  {key_expr : val_expr for i in seq}
'''d={i:i for i in range(1,5)}
print(d)
'''
'''d={i:i*i for i in range(1,5)}
print(d)
'''
'''import math
def isprime2(n,i):
    if n<2:
        return False
    if i==1:
        return True
    elif n%i==0:
        return False
    else:
        i=i-1
        return  isprime2(n,i)
d={i:math.factorial(i) for i in range(1,11) if isprime2(i,i//2)}
print(d)
'''
'''import math
def isprime1(n):
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    return factors==2
d={i:math.factorial(i) for i in range(1,11) if isprime1(i)}
print(d)
'''
'''import math
def isprime1(n):
    factorial=0
    for i in range(1,11):
        if n%i==0:
            factorial+=1
    return factorial==2
d={i:math.factorial(i) for i in range(1,11) if not isprime1(i)}
print(d)
'''
# class-25
# =========
# chapter-05:- List (array)
# ---------------------------
# Q1. sum of elements present in the given list
'''def sum(l):
    s=0
    for i in l:
        s+=i
    return s
l=[1,2,3]
print(sum(l))
'''
# Q2. Average of elements present in the list
'''def average(l):
    if len(l)==0:
        return 0.0
    else:
        s=0
        for i in l:
            s+=i
        return s/len(l)
l=[1,2,3,4,5]
print(average(l))
l=[]
print(average(l))
'''
# Q3. seperate even and odd elements from a list
'''def fun(l):
    l1=[]
    l2=[]
    for i in l:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
    return l1,l2
l=[1,2,3,4,5,6,7,8,9,10]
print(fun(l))
'''
'''def fun(l):
    l1=[x for x in l if x%2==0]
    l2=[x for x in l if x%2!=0]
    print(l1)
    print(l2)
l=[1,2,3,4,5,6,7,8,9,10]
fun(l)
'''
'''def fun(l):
    l1=[x for x in l if x%2==0]
    l2=[x for x in l if x%2!=0]
    return l1,l2
l=[1,2,3,4,5,6,7,8,9,10]
even,odd=fun(l)
print(even)
print(odd)
'''
# Q4. generate a lists with even and odd elements in the range of 0 to 10 inclusive
'''def fun():
    l1=[x for x in range(0,11) if x%2==0]
    l2=[x for x in range(0,10+1) if x%2!=0]
    return l1,l2
even,odd=fun()
print(even)
print(odd)
'''
# class-27
# ========
# Q5. get smaller elements from a list lesser then the given element x
'''def fun(l):
    l1=[]
    x=10 
    for i in l:
        if i<x:
            l1.append(i)
    return l1
l=[9,11,15,12,3,7,14,10]
print(fun(l))
'''
'''def fun(l,x):
    l1=[i for i in l if i<x]
    return l1
l=[9,11,15,12,3,7,14,10]
x=10
print(fun(l,x))
'''
# Q6. generate 10 random number from 1 to 20 inclusive and append them to the list
'''import random
def fun():
    l=[]
    for i in range(10):
        l.append(random.randint(1,20))
    return l
print(fun())
'''
# Q7. swap frist and last element in the list
'''def fun(l):
    l[0],l[len(l)-1]=l[len(l)-1],l[0]
    # l[0],l[-1]=l[-1],l[0]
    return l
l=[1,2,3,4,5]
print(fun(l))
'''
# roof
'''l=[1,2,3]
t=(4,5,6)
print(l+t)   #error
l+=t
print(l)
print(t)
'''
# Q8. count no of elements greater than x
'''def fun(l,x):
    count=0
    for i in l:
        if i>x:
            count+=1
    return count
l=[1,2,3,4,5]
x=2
print(fun(l,x))
'''
'''def fun(l,x):
    return len([i for i in l  if i>x])
l=[1,2,3,4,5]
x=2
print(fun(l,x))
'''
# Q9. reverse the given list
'''def fun(l,s,e):
    while s<=e:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1
l=[1,2,3,4,5]
print(l)
fun(l,0,len(l)-1)
print(l)
'''
'''def fun(l):
    return l.reverse()
l=[1,2,3,4,5]
fun(l)
print(l)
'''
'''def fun(l):
    return l[::-1]
l=[1,2,3,4,5]
print(fun(l))
'''
'''def fun(l):
    l[:]=l[::-1]
l=[1,2,3,4,5]
fun(l)
print(l)
'''
# class-28
# ======
# Q10. get the index of the given element
'''def fun(l,x):
    for i in range(len(l)):
        if x==l[i]:
            return i
    return None
l=[1,2,3,4,5]
x=2
print(fun(l,x))
'''
'''def fun(l,x):
    if x in l:
        return l.index(x)
    else:
        return None
l=[1,2,3,4,5]
x=3
print(fun(l,x))
'''
# Q11. find the largest/max element in a list
'''def largest(l):
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max
l=[1,5,12,14,3]
print(largest(l))       
'''
# Q12. find second max/largest element
'''def fun1(l):
    max=l[0]
    for i in range(1,len(l)):
        if max<i:
            max=i
    return max
def fun2(l):
    max=fun1(l)
    smax=None
    for i in l:
        if i!=max:
            if smax==None:
                smax=i
            else:
                smax=smax if smax>i else i
    return smax
l=[1,5,2,14,3]
print(fun2(l))
'''
'''def fun(l):
    l.sort()
    return l[-2]
l=[1,5,12,14,13]
print(fun(l))
'''
'''def fun(l):
    largest=float('-inf')
    second=float('-inf')
    for i in l:
        if i>largest:
            second=largest
            largest=i
        elif i > second:
            second=i
    return second
l=[1,5,12,14,13]
print(fun(l))
'''
# Q13. check  if a list is sorted list or not
'''def fun(l):
    i=1
    while i<len(l):
        if l[i]<l[i-1]:
            return False
        i=i+1
    return True
l=[1,2,3,4,5]
print(fun(l))
l=[1,3,2,4,5]
print(fun(l))
'''
'''def fun(l):
    l1=sorted(l)
    return l==l1
l=[1,2,3,4,5]
print(fun(l))
'''
# Q14. remove duplicate elements from a list
'''def fun(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
l=[1,2,3,4,4,5]
print(fun(l))
'''
# Q15.left rotate a list by one element
'''l=[1,2,3,4,5]
l=l[1:]+l[0:1]
print(l)
'''
'''l=[1,2,3,4,5]
l.append(l.pop(0))
print(l)
'''
'''def leftrotatebyone(l):
    n=len(l)
    x=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x
l=[1,2,3,4,5]
leftrotatebyone(l)
print(l)
'''
'''def left_rotate(l, n):
    n=n%len(l)
    l=l[n:]+l[:n]
    return l
l=[1,2,3,4,5]
n=2
print(left_rotate(l,n))
'''
'''def left_rotate(l, n):
    n=n%len(l)
    for _ in range(n):
        first=l.pop(0)
        l.append(first)
    return l
l=[1,2,3,4,5]
n=2
print(left_rotate(l,n))
'''
# Q16. right rotate a list by one list
'''l=[11,55,22,66,44]
# l=l[-1]+l[0 :len(l)-1]     #error
# l=[l[-1]+l[0:lren(l)-1]]
l=l[-1:-2:-1]+l[0:len(l)-1]
print(l)
'''
'''l=[11,55,22,66,44]
l.insert(0,l.pop(-1))
print(l)
'''
'''def rightRotateByOne(l):
    n=len(l)
    x=l[n-1]
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    l[0]=x
l=[1,2,3,4,5]
rightRotateByOne(l)
print(l)
'''
# class-29
# ======
# Q17.left rotate a list by 'd' places
'''l=[1,2,3,4,5]
d=int(input())
l=l[d:]+l[:d]
print(l)
'''
'''from collections import deque
l=[1,2,3,4,5]
d=int(input())
dq=deque(l)
dq.rotate(-d)             #note:- -d indicates left rotation & +d indicates right rotation
l=dq
print(l)
l=list(dq)
print(l)
'''
'''def leftrotatemethod1(l,d):
    for i in range(0,d):
        l.append(l.pop(0))
l=[1,2,3,4,5]
d=2
leftrotatemethod1(l,d)
print(l)
'''
'''def reverse(l,b,e):
    while b<e:
        l[b],l[e]=l[e],l[b]
        b+=1
        e-=1
def fun(l,d):
    n=len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)
l=[1,2,3,4,5]
d=int(input())
fun(l,d)
print(l)
'''
# Q18. right rotate a list by 'd' places
'''def reverse(l,b,e):
    while b<e:
        l[b],l[e]=l[e],l[b]
        b+=1
        e-=1
def fun(l,d):
    n=len(l)
    reverse(l,0,n-1)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
l=[1,2,3,4,5,6]
d=int(input("enter a no of rotations:"))
fun(l,d)
print(l)
'''
'''def fun(l,d):
    for i in range(0,d):
        l.insert(0,l.pop(-1))
l=[1,2,3,4,5,6]
d=int(input("enter a no of rotations:"))
fun(l,d)
print(l)
'''
'''l=[1,2,3,4,5]
d=int(input("enter a no of rotations:"))
l=l[len(l)-d:]+l[:len(l)-d]
print(l)
'''
'''from collections import deque
l=[1,2,3,4,5]
d=int(input("enter a no of rotations:"))
dq=deque(l)
dq.rotate(d)
print(dq)
l=list(dq)
print(l)
'''
# Q19. merge two list into third list
'''def fun(l1,l2):
    l3=[]
    for i in l1:
        l3.append(i)
    for i in l2:
        l3.append(i)
    return l3
l1=[1,3,5,2,4]
l2=[6,8,7,9,10]
print(fun(l1,l2))
'''
'''def fun(l1,l2):
    return l1+l2
l1=[1,2,3,4]
l2=[5,6,7,8,9]
l3=fun(l1,l2)
print(l3)
'''
# Q20.merge two list into third list and sort
'''def fun(l1,l2):
    l=l1+l2
    l.sort()
    return l
l1=[1,3,5,7,9]
l2=[2,4,6,8]
l3=fun(l1,l2)
print(l3)
'''
# Q21. who has the majoarity?
# gievn a list of size n and return an elements postion which appears greater than n/2times
'''def fun(l):
    n=len(l)
    for i in range(0,n):
        count=1
        for j in range(i+1,n):
            if l[i]==l[j]:
                count+=1
        if count >n/2:
            return l[i]
    return -1
print(fun([8,3,4,8,8]))
print(fun([8,7,6,8,6,6,6,6]))
print(fun([3,7,4,7,7,5]))
'''
# Q22,find union of two list objects
'''def fun(l1,l2):
    l=[]
    for i in l1:
        if i not in l:
            l.append(i)
    for j in l2:
        if j not in l:
            l.append(j)
    return l
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l3=fun(l1,l2)
print(l3)
'''
# Q23.find intersection of two lists objects
'''def fun(l1,l2):
    l=[]
    for i in l1:
        if i in l2:
            l.append(i)
    return l
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l3=fun(l1,l2)
print(l3)
'''
# class-30
# ======
# Chapter-6:- matrics programs
# ----------------------------------
# Q1.read and write matrics
'''m=int(input("enter no of rows:"))
n=int(input("enter no of columns:"))
l=[]
for i in range(m):
    tl=[int(i) for i in input().split()]
    l.append(tl)
print(l)
'''
'''m=int(input("enter no of rows:"))
n=int(input("enter no of columns:"))
l=[]
for i in range(m):
    tl=[int(j) for j in input().split()]
    l.append(tl)
for i in range(m):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
'''
'''def read(l,m,n):
    for i in range(m):
        tl=[int(i) for i in input().split()]
        l.append(tl)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter a no of rows:"))
n=int(input("enter  a no of cols:"))
l=[]
read(l,m,n)
printm(l,m,n)
'''
# Q2.sum of each element in matrix
'''def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
def sumofelements(l,m,n):
    s=0
    for i in range(m):
        s+=sum(l[i])
    return s
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
print(sumofelements(l,m,n))
'''
# Q3.addition of two elements
'''def addition(l1,m,n,l2,l3):
    for i in range(m):
        for j in range(n):
            l3[i][j]=l1[i][j]+l2[i][j]
def read(l,m,n):
    for i in range(m):
        tl=[int(i) for i in input().split()]
        l.append(tl)
def init(l,m,n):
    for i in range(n):
        temp=[0 for i in range(n)]
        l3.append(temp)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l1=[]
read(l1,m,n)
l2=[]
read(l2,m,n)
l3=[]
init(l3,m,n)
addition(l1,m,n,l2,l3)
print("Matrix-A")
printm(l1,m,n)
print("Matrix-B")
printm(l2,m,n)
print("Matrix-c")
printm(l3,m,n)
'''
# Q4.substraction of two matrics
'''def subtraction(m,n,l1,l2,l3):
    for i in range(m):
        for j in range(n):
            l3[i][j]=l1[i][j]-l2[i][j]
def read(l,m,n):
    for i in range(m):
        tl=[int(i) for i in input().split()]
        l.append(tl)
def init(l,m,n):
    for i in range(m):
        temp=[0 for i in range(n)]
        l.append(temp)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter a rows:"))
n=int(input("enter a cols:"))
l1=[]
read(l1,m,n)
l2=[]
read(l2,m,n)
l3=[]
init(l3,m,n)
subtraction(m,n,l1,l2,l3)
print("Matrix-A")
printm(l1,m,n)
print("Matrix-B")
printm(l2,m,n)
print("Subtraction-Matrix")
printm(l3,m,n)
'''
# Q5.Multipliaction of two characters
'''def multiplication(l1,m,n,l2,l3):
    for i in range(m):
        for j in range(n):
            for k in range(n):  #or m
                l3[i][j]=l3[i][j]+l1[i][k]*l2[k][j]
def init(l,m,n):
    for i in range(m):
        temp=[0 for i in range(n)]
        l.append(temp)
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l1=[]
read(l1,m,n)
l2=[]
read(l2,m,n)
l3=[]
init(l3,m,n)
multiplication(l1,m,n,l2,l3)
print("Matrix-A")
printm(l1,m,n)
print("Matrix-B")
printm(l2,m,n)
print("Matrix-c")
printm(l3,m,n)
'''
# normal multiplication
'''def multiplication(l1,m,n,l2,l3):
    for i in range(m):
        for j in range(n):
            l3[i][j]=l1[i][j]*l2[i][j]
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
def init(l,m,n):
    for i in range(m):
        tl=[0 for i in range(n)]
        l3.append(tl)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l1=[]
read(l1,m,n)
l2=[]
read(l2,m,n)
l3=[]
init(l3,m,n)
multiplication(l1,m,n,l2,l3)
print("Matrix-A")
printm(l1,m,n)
print("Matrix-B")
printm(l2,m,n)
print("Multipliaction")
printm(l3,m,n)
'''
# Q6.row wise sum calculation
'''def rowwisesum(l,m,n):
    for i in range(m):
        s=0
        for j in range(n):
            s=s+l[i][j]
        print(f"{i} row sum:{s}")
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
printm(l,m,n)
rowwisesum(l,m,n)
'''
# Q7.cols wise sum calculation
'''def colwisesum(l,m,n):
    for i in range(m):
        s=0
        for j in range(n):
            s=s+l[j][i]
        print(f"{i} col sum:{s}")
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
colwisesum(l,m,n)
'''
# Q8. sum of diagonal elements
'''def diagonalsum(l,m,n):
    s=0
    for i in range(m):
        for j in range(n):
            if i==j:
                s=s+l[i][j]
    return s
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
print(diagonalsum(l,m,n))
''' 
# Q9.sum of opposite diagonal elements
'''def diagonalsum(l,m,n):
    s=0
    for i in range(m):
        s=s+l[i][i]
    return s
def opdiagonalsum(l,m,n):
    s=0
    for i in range(m):
        s=s+l[i][m-i-1]
    return s
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
m=int(input("enter  no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
print(diagonalsum(l,m,n))
print(opdiagonalsum(l,m,n))
'''
# Q10. Transpose of given matrix
'''def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[j][i],end=" ")
        print()
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
print("Transpose Matrix")
printm(l,m,n)
'''
# Q.Roof:-print two digaonals but no repeat the middle values
'''def twoOpdigonalsum(l,m,n):
    s=0
    for i in range(m):
        s=s+l[i][i]+l[i][m-i-1]
    return s-l[m//2][n//2]
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
print(twoOpdigonalsum(l,m,n))
'''
