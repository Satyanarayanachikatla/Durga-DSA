# class-2
'''a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
sum=a+b+c
print(f"total sum ={sum}")
'''
'''s=input("enter a string:")
print(s)
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
'''
# 1.to read a string and convert all even indexed values into upper case
'''def myfun(s):
    l=list(s)
    ll=[]
    for i in range(len(s)):
        if i%2==0:
            ll.append(l[i].upper())
        else:
            ll.append(l[i].lower())
    return ll
s=input("enter a string:")
print(myfun(s))
'''
# ------------------------------------------------------
'''def myfun(s):
    l=list(s.lower())
    for i in range(len(s)):
        if i%2==0:
            l[i]=l[i].upper()
    return "".join(l)
s=input("enter a string:")
print(myfun(s))
'''
'''s=input("enter a string:")
modify_string=""
count=0
for i in s:
    if count%2==0:
        modify_string+=i.upper()
        count+=1
    else:
        modify_string+=i.lower()
        count+=1
print(modify_string)
'''
# to find sum of all elements present in a list
'''from functools import reduce
def fun1(l):
    s=0
    for i in l:
        s+=i
    return s
def fun2(l):
    return sum(l)
def fun3(l):
    return reduce(lambda i,j:i+j,l)
x=[1,2,3]
print(fun1(x))
print(fun2(x))
print(fun3(x))
'''
# to find max of two numbers
'''def max1(a,b):
    if a>b:
        return a
    else:
        return b
def max2(a,b):
    return max(a,b)
def max3(a,b):
    return a if a>b else b
def max4(a,b):
    call=lambda a,b:a if a>b else b
    return call(a,b)
def max5(a,b):
    l=[]
    l.append(a)
    l.append(b)
    return max(l)
a=int(input("enter 'a' number:"))
b=int(input("enter 'b' number:"))
print(max1(a,b))
print(max2(a,b))
print(max3(a,b))
print(max4(a,b))
print(max5(a,b))
'''
# Time complexity
'''def fun(n):
    c=0
    i=0
    while i<n:    #---->Time Complexity:O(n)
        c+=1
        i+=1
    return c                              
print("n=100,number of instructions in o(n):",fun(100))
'''
'''def fun(n):
    c=0
    i=0
    while i<n:  #---->O(n)
        j=0
        while j<n:   #---->O(n)
            c+=1
            j+=1
        i+=1
    return c                 #--------->Time Complexity:O(n)
print("n=100,number of instructions in O(n):",fun(100))
'''
# To find max of three numbers
'''def max1(a,b,c):
    return max(a,b,c)
def max2(a,b,c):
    if a>b:
        if a>c:
            return a
    elif b>c:
        if b>a:
            return b
    return c
def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(max1(a,b,c))
print(max2(a,b,c))
print(max3(a,b,c))
''' 
# To find max of four numbers
'''def max1(a,b,c,d):
    return a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
print(max1(a,b,c,d))
'''
# To find max of five numbers
# To find min of three numbers
# To find min of four numbers
# To find min of five numbers
# to find difference b/w max and min of five numbers
'''def findDiff(a,b,c,d,e):
    find_Diff=lambda a,b,c,d,e:max(a,b,c,d,e)-min(a,b,c,d,e)
    return find_Diff(a,b,c,d,e)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
e=int(input("e:"))
print(findDiff(a,b,c,e,d))
'''
# class-5
# ---------

# to find factorial of the given number
'''def fact1(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    return fact
def fact2(n):
    if n==0:
        return 1
    else:
        return n*fact2(n-1)
import math
def fact3(n):
    return math.factorial(n)
for i in range(10+1):
    print(i,fact1(i),fact2(i),fact3(i),sep='\t')
'''
# ----------OR---------------------
'''n=int(input("enter a number:"))
print(fact1(n))
print(fact2(n))
print(fact3(n))
'''

# class-6
# ----------
# to check give number is prime or not
'''def isprime1(n):
    factor=0
    for i in range(1,n+1):
        if n%i==0:
            factor+=1
    return factor==2
def isprime2(n,i):
    if n<=1:
        return False
    elif i==1:
        return True
    elif n%i==0:
        return False
    else:
        i=i-1
        return isprime2(n,i)
# n=int(input("enter a number:"))
# print(isprime1(n))
# print(isprime2(n,n//2))

for i in range(2,11):
    print(f"i={i} \t {isprime1(i)} \t {isprime2(i,i//2)}")
'''

# to extract digits present in the given number
'''n=int(input("enter a number:"))
while n!=0:
    d=n%10
    print(d)
    n=n//10
'''
# class-7
# ==========
# sum of digits present in the given number
'''def digits1(n):
    s=0
    while n!=0:
        digit=n%10
        s+=digit
        n=n//10
    return s
def digits2(n):
    return sum([int(i) for i in str(n)])
n=int(input("enter a number:"))
print(digits1(n))
print(digits2(n))
'''
# reverse of the give number
'''def reverse1(n):
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
def reverse2(n):
    return int(str(n)[::-1])
n=int(input("enter a number:"))
print(reverse1(n))
print(reverse2(n))
'''
# class-8
# ======
# given number is palindrome or not
'''def ispalin1(n):
    original=n
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev==original
def ispalin2(n):
    s=str(n)
    return s==s[::-1]
    # return n==int(str(n)[::-1])
n=int(input("enter a number:"))
print(ispalin1(n))
print(ispalin2(n))
'''
# class-9
# ==========
# CLASS-10
# ============
# class-11
# =========
# chapter-02:-Approach to solve problems
# ============================
# class-12
# =======
# chapter-13:-sample algorithms and implementation
# ===================================
# class-13:
# =======
# even or odd
'''def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
def check1(n):
    if (n&1)!=0:
        return "odd"
    else:
        return "even"
n=int(input("enter a number:"))
print(check(n))
print(check1(n))
'''
# Max of two numbers
'''def max_v1(a,b):
    if a>b:
        return a
    else:
        return b
def max_v2(a,b):
    return a if a>b else b
def max_v3(a,b):
    result=lambda a,b:a if a>b else b
    return result(a,b)
def max_v4(a,b):
    return max(a,b)
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(max_v1(a,b))
print(max_v2(a,b))
print(max_v3(a,b))
print(max_v4(a,b))
'''
# Anonymous functions or lambda functions
'''def add(a,b):
    return a+b
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(add(a,b))
'''
'''result=lambda a,b:a+b
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(result(a,b))
'''
# min of two numbers
# max of three numbers
# min of three numbers
# max of four numbers
'''def max_v1(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>c and b>d:
        return b
    elif c>d:
        return c
    else:
        return d
def max_v2(a,b,c,d):
    return a if a>b and b>c and a>d else b if b>c and b>d else c if c>d else d
def max_v3(a,b,c,d):
    result=lambda a,b,c,d:a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
    return result(a,b,c,d)
def max_v4(a,b,c,d):
    return max(a,b,c,d)
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=int(input("enter a number:"))
print(max_v1(a,b,c,d))
print(max_v2(a,b,c,d))
print(max_v3(a,b,c,d))
print(max_v4(a,b,c,d))
'''
# min of four numbers
# min of five numbers
# max of five numbers
'''def max_v1(a,b,c,d,e):
    if a>b and a>c and a>d and a>e:
        return a
    elif b>c and b>d and b>e:
        return b
    elif c>d and c>e:
        return c
    elif d>e:
        return d
    else: 
        return e
def max_v2(a,b,c,d,e):
    return a if a>b and a>c and a>d and a>e else b if b>c and b>d and b>e else c if c>d and c>e else d if d>e else e
def max_v3(a,b,c,d,e):
    result=lambda a,b,c,d,e:a if a>b and a>c and a>d and a>e else b if b>c and b>d and b>e else c if c>d and c>e else d if d>e else e
def max_v4(a,b,c,d,e):
    return max(a,b,c,d,e) 
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=int(input("enter a number:"))
e=int(input("enter a number:"))
print(max_v1(a,b,c,d,e))
print(max_v2(a,b,c,d,e))
print(max_v3(a,b,c,d,e))
print(max_v4(a,b,c,d,e))
'''
# swapping of two integer values
'''def swap_v1(a,b):
    print(f"before swapping :a={a} and b={b}")
    a,b=b,a
    print(f"after swapping :a={a} and b={b}")
def swap_v2(a,b):
    print(f"before swapping :a={a} and b={b}")
    temp=a
    a=b
    b=temp
    print(f"after swapping :a={a} and b={b}")
def swap_v3(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(f"after swapping :a={a} and b={b}")
def swap_v4(a,b):
    a=a*b
    b=a//b
    a=a//b
    print(f"after swapping :a={a} and b={b}")
def swap_v5(a,b):
    print(f"before swapping :a={a} and b={b}")
    a=a^b
    b=a^b
    a=a^b
    print(f"after swapping :a={a} and b={b}")
def swap_v6(a,b):
    a=a+b-(b:=a)
    print(f"after swapping :a={a} and b={b}")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
swap_v1(a,b) 
swap_v2(a,b)
swap_v3(a,b) 
swap_v4(a,b)  
swap_v5(a,b)
swap_v6(a,b)
'''
# recursion
'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n* fact(n-1)
x=fact(3)
print(x)
'''
# class-15
# =======
# Absolute value
'''def abs_v1(n):
    if n<0:
        return -n
    else:
        return n
def abs_v2(n):
    return abs(n)
n=int(input("enter a number:"))
print(abs_v1(n))
print(abs_v2(n))
'''
# sum of n natural numbers
'''def sum_v1(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
def sum_v2(n):
    return n*(n+1)//2
def sum_v3(n):
    if n==0:
        return 0
    else:
        return n+sum_v3(n-1)
n=int(input("enter a number:"))
print(f"number={n} and sum={sum_v1(n)}")
print(f"number={n} and sum={sum_v2(n)}")
print(f"number={n} and sum={sum_v3(n)}")
'''
# factorial of given number
'''import math
def fact_v1(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def fact_v2(n):
    return math.factorial(n)
def fact_v3(n):
    if n==0:
        return 1
    else:
        return n*fact_v3(n-1)
n=int(input("enter a number:"))
print(f"number={n} and factorial={fact_v1(n)}")
print(f"number={n} and factorial={fact_v2(n)}")
print(f"number={n} and factorial={fact_v3(n)}")
'''
# digits extraction
'''def digits_v1(n):
    while n!=0:
        print(n%10)
        n=n//10
def digits_v2(n):
    s=str(n)
    for i in s[::-1]:
        print(i)
n=int(input("enter a number:"))
digits_v1(n)
digits_v2(n)
'''
# count digits
'''def count_v1(n):
    c=0
    while n!=0:
        c=c+1
        n=n//10
    return c
def count_v2(n):
    return len(str(n))
def count_v3(n):
    if n==0:
        return 0
    else:
        return 1+count_v3(n//10)
n=int(input("enter a number:"))
print(f"number={n} and count of digits={count_v1(n)}")
print(f"number={n} and count of digits={count_v1(n)}")
print(f"number={n} and count of digits={count_v1(n)}")
'''
# reverse a number
'''def rev_v1(n):
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
def rev_v2(n):
    return str(n)[::-1]
n=int(input("enter a  number:"))
print(rev_v1(n))
print(rev_v2(n))
'''
# palindrome number
'''def ispali_v1(n):
    t=n
    r=0
    while t!=0:
        digit=t%10
        r=r*10+digit
        t=t//10
    return n==r
def ispali_v2(n):
    return str(n)==str(n)[::-1]
n=int(input("enter  a number:"))
print(ispali_v1(n))
print(ispali_v2(n))
n=int(input("enter a number:"))
print(f"original={n} nd ispali={ispali_v1(n)}")
print(f"original={n} nd ispali={ispali_v2(n)}")
'''
# trailing zeros of factorial
'''import math
def fun(n):
    f=math.factorial(n)
    c=0
    while f!=0:
        if f%10!=0:
            break
        c=c+1
        f=f//10
    return c
def fun2(n):
    f=str(math.factorial(n))[::-1]
    c=0
    for i in f:
        if i!='0':
            break
        c=c+1
    return c
n=int(input("enter a number:"))
print(f"number={n} fact={math.factorial(n)} and training 0's={fun(n)}")
'''
# class-17
# ======
# iterative power (or) x to the power y
'''import math
def power_v1(x,y):
    res=1
    for i in range(1,y+1):
        res=res*x
    return res
def power_v2(x,y):
    return x**y
def power_v3(x,y):
    return math.pow(x,y)
x=int(input("enter a number:"))
y=int(input("enter a number:"))
print(f"x={x},y={y} and {x} to the power {y} iss :{power_v1(x,y)}")
print(f"x={x},y={y} and {x} to the power {y} iss :{power_v2(x,y)}")
print(f"x={x},y={y} and {x} to the power {y} iss :{power_v3(x,y)}")
'''
# sum of digits
'''def sum_v1(n):
    sum=0
    while n!=0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
def sum_v2(n):
    return sum([int(i) for i in str(n)])
n=int(input("enter a number:"))
print(f"n={n} and sum of digits is :{sum_v1(n)}")
print(f"n={n} and sum of digits is :{sum_v2(n)}")
'''
# sum of even digits
'''def sum_v1(n):
    sum=0
    while n!=0:
        digit=n%10
        if digit%2==0:
            sum+=digit
        n=n//10
    return sum
def sum_v2(n):
    return sum([int(i) for i in str(n) if int(i)%2==0])
n=int(input("enter  a number:"))
print(sum_v1(n))
print(sum_v2(n))
'''
# sum of odd digits
'''def sum_v1(n):
    sum=0
    while n!=0:
        digit=n%10
        if digit%2!=0:
            sum+=digit
        n=n//10
    return sum
def sum_v2(n):
    return sum([int(i) for i in str(n) if int(i)%2!=0])
n=int(input("enter  a number:"))
print(sum_v1(n))
print(sum_v2(n))
'''
# sum of prime digits
'''def sum_v1(n):
    s=0
    while n!=0:
        d=n%10
        if d==2 or d==3 or d==5 or d==7:
            s+=d
        n=n//10
    return s
def sum_v2(n):
    return sum([int(i) for i in str(n) if i in "2357" ])
n=int(input("enter a  number:"))
print(f"n={n} and sum of prime digits is:{sum_v1(n)}")
print(f"n={n} and sum of prime digits is:{sum_v2(n)}")
'''
# prime nuber or not
'''def prime_v1(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=1
    return f==2
def prime_v2(n,i):
    if i==1:
        return True
    elif n%i==0:
        return False
    else:
        return prime_v2(n,i-1)
n=int(input("enter a number:"))
print(f"n={n} and it is prime:{prime_v1(n)}")
print(f"n={n} and it is prime:{prime_v2(n,n//2)}")
'''
# prime factorization
'''def factorization(n):
    l=[]
    i=2
    while n>1:
        if n%i==0:
            l.append(i)
            n=n//i
        else:
            i=i+1
    return l
n=int(input("entera number:"))
print(factorization(n))
'''
# all divisors of n
'''def divisors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l
n=int(input("enter a number:"))
print(f"n={n} and divisor :{divisors(n)}")
'''
# perfect number
# power of x to n
# fibbnoic series
# trib number
# class-18
# ========
# perfect number
'''def isperfect_v1(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return n==s
def isperfect_v2(n):
    l=divisors(n)
    return n==sum(l)
def divisors(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return l
n=int(input("enter a number:"))
print(f"n={n} and divisors:{isperfect_v1(n)}")
print(f"n={n} and divisors:{isperfect_v2(n)}")
'''
# power of x  to n
'''def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
print(power(2,3))
'''
# 1 to 1000 perfect numbers
'''def divisors(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return l
def isperfect(n):
    l = divisors(n)
    return n == sum(l)
for i in range(1, 1001):
    if isperfect(i):
        print(i)
'''
# armstrong number
'''def armstrong(n):
    l=len(str(n))
    s=0
    t=n
    while n!=0:
        digit=n%10
        s=s+digit**l
        n=n//10
    return s==t
for i in range(1,1001):
    if armstrong(i):
        print(i)
'''
# strong number
'''import math
def strong(n):
    s=0
    t=n
    while n!=0:
        d=n%10
        s=s+math.factorial(d)
        n=n//10
    return s==t
for i in range(1,100001):
    if strong(i):
        print(i)
'''
# fib sequence
'''def fib(n):
    l=[]
    a=0
    b=1
    l.append(a)
    l.append(b)
    for i in range(n-2):
        c=a+b
        l.append(c)
        a=b
        b=c
    return l
s=int(input("enter a number:"))
print(fib(s))
'''
# tribnoic sequence
'''def trib(n):
    l=[]
    a=0
    b=1
    c=2
    l.append(a)
    l.append(b)
    l.append(c)
    for i in range(n-3):
        d=a+b+c
        l.append(d)
        a=b
        b=c
        c=d
    return l
print(trib(6))
'''
'''def trib(n):
    a=0
    b=1
    c=2
    for i in range(n):
        print(a,end=" ")
        a,b,c=b,c,a+b+c
trib(6)
'''
