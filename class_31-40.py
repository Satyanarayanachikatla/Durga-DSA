# Class-31
# ========
# Q11.Identify matrix or not
'''def fun(l,m,n):
    for i in range(m):
        for j in range(n):
            if i==j and l[i][j]!=1:
                return False
            if i!=j and l[i][j]!=0:
                return False
    return True
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
print(fun(l,m,n))
'''
# Q12.swapping of two rows
'''def fun(l,m,n,x,y):
    l[x-1],l[y-1]=l[y-1],l[x-1]
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
x=int(input("enete a row1:"))
y=int(input("enter a row2:"))
fun(l,m,n,x,y)
printm(l,m,n)
'''
# Q13.swaping of two cols
'''def fun(l,m,n,x,y):
    for i in range(m):
        l[i][x-1],l[i][y-1]=l[i][y-1],l[i][x-1]
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
x=int(input("enter col1:"))
y=int(input("enter col2:"))
fun(l,m,n,x,y)
printm(l,m,n)
'''
# Q14.swaping diagonal elements
'''def fun(l,m,n,x,y):
    for i in range(m):
        l[i][i],l[i][m-i-1]=l[i][m-i-1],l[i][i]
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
m=int(input("enter  no of rows:"))
n=int(input("enter no of cols:"))
l=[]
read(l,m,n)
x=int(input("enter a diagonal1:"))
y=int(input("enter a diagonal2:"))
fun(l,m,n,x,y)
printm(l,m,n)
'''
# Q15.rotate matrix by 90 degress-->anticlockwise
'''def fun(l,m,n):
    tl=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(m):
        for j in range(n):
            tl[i][j]=l[j][i]
    printmm(tl,m,n)
def printmm(l,m,n):
    for i in range(m-1,-1,-1):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
def read(l,m,n):
    for i in range(m):
        temp=[int(i) for i in input().split()]
        l.append(temp)
def printm(l,m,n):
    for i in range(m):
        for j in range(n):
            print(l[i][j],end=" ")
        print( )
m=int(input("enter no of rows:"))
n=int(input("enter no of cols:"))
l1=[]
read(l1,m,n)
# printm(l1,m,n)
print("90 degrees")
fun(l1,m,n)
'''
# 90° clockwise rotation
'''def fun(l,m,n):
    tl = [[0 for j in range(m)] for i in range(n)]

    # transpose
    for i in range(m):
        for j in range(n):
            tl[j][i] = l[i][j]

    # reverse every row
    for i in range(n):
        tl[i].reverse()
    printm(tl,n,m)
def read(l,m,n):
    for i in range(m):
        temp = [int(x) for x in input().split()]
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
print("Original matrix:")
printm(l1,m,n)
print("After 90 degree clockwise rotation:")
fun(l1,m,n)
'''
'''def rotate90(l, m, n):
    tl = [[0 for j in range(m)] for i in range(n)]

    # transpose
    for i in range(m):
        for j in range(n):
            tl[j][i] = l[i][j]

    # reverse every row
    for i in range(n):
        tl[i].reverse()
    return tl
def fun(l, m, n, degree):
    if degree == 90:
        l = rotate90(l, m, n)
        printm(l, n, m)
    elif degree == 180:
        l = rotate90(l, m, n)
        l = rotate90(l, n, m)
        printm(l, m, n)
    elif degree == 270:
        l = rotate90(l, m, n)
        l = rotate90(l, n, m)
        l = rotate90(l, m, n)
        printm(l, n, m)
    elif degree == 360:
        printm(l, m, n)
    else:
        print("Enter only 90, 180, 270 or 360")
def read(l, m, n):
    for i in range(m):
        temp = [int(x) for x in input().split()]
        l.append(temp)
def printm(l, m, n):
    for i in range(m):
        for j in range(n):
            print(l[i][j], end=" ")
        print()
m = int(input("Enter no of rows: "))
n = int(input("Enter no of cols: "))
l1 = []
read(l1, m, n)
print("Original matrix:")
printm(l1, m, n)
degree = int(input("Enter rotation degree (90/180/270/360): "))
print("Rotated matrix:")
fun(l1, m, n, degree)
'''
# chapter-7:- Recursion
# ===============
'''def fun(n):
    print("satya")
    fun(n-1)
fun(3)                         #RecursionError: maximum recursion depth exceeded
'''
'''def fun(n):
    if n==0:
        return 
    print("satya")
    fun(n-1)
fun(3)
'''
'''def fun(n):
    if n<=0:
        return 
    print("satya")
    fun(n-1)
fun(-3)                              #empy
'''
# class-32:-
# ======
# factorial of the given number
'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(4))
'''
# fibnnoic number
'''def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(6))
'''
# Tail Recursion--->A function calls itself as the very last operation before returning.
# (or) Function lo recursive call chesina taruvatha ఇంకేమీ పని ఉండకూడదు. అదే Tail Recursion.
'''def fun(n):
    if n<=0:
        return
    print(n,end="")
    fun(n-1)
fun(3)
'''
# non-trail recursion--->So the recursive call is NOT the last complete operation.,Therefore, this is not tail recursion.
'''def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n,end="")
fun(3)
'''
# ex-1:-print natural numbers from 1 to n
'''def fun(n):
    if n<=0:
        return 
    fun(n-1)
    print(n)
fun(3)
'''
# ex-2:-print natural numbers from n to 1
'''def fun(n):
    if n<=0:
        return 
    print(n)
    fun(n-1)
fun(3)
'''
# ex-3:-sum of digits
'''def fun(n):
    if n<10:
        return n
    return n%10+fun(n//10)
print(fun(123))
'''
# Ex-4:-sum of n natural numbers
'''def fun(n):
    if n<=0:
        return 0
    return n+fun(n-1)
print(fun(4))
'''
# Ex-5:-string palindrome
'''def pali(s,start,end):
    if start>=end:
        return True
    return s[start]==s[end] and pali(s,start+1,end-1)
print(pali("sir",0,2))
print(pali("madam",0,4))
'''
# ex-7:-claculate  a power b
'''def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,0))
print(power(0,2))
print(power(2,3))
'''
# Ex-8:-prime number application
'''def prime(n,i):
    if i==1:
        return True
    elif n%i==0:
        return False
    return prime(n,i-1)
print(prime(4,4//2))
print(prime(5,5//2))
'''
# Ex-9:-fibbonic seq
'''def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
for  i in range(11):
    print(fib(i),end=" ")
'''
# ex-10:-reverse of string
'''def fun(s):
    if len(s)==0 or len(s)==1:
        return s
    return fun(s[1:])+s[0]
print(fun("praksh"))
'''
# class-33
# =========
# Ex:-permutations of given string
'''def permutations(s,ans):
    if len(s)==0:
        print(ans)
        return
    for i in range(0,len(s)):
        permutations(s[:i]+s[i+1:],ans+s[i])
permutations("abc","")
'''
# count also count in how many combinations
'''def permutations(s,ans):
    global c
    if len(s)==0:
        c=c+1
        print(ans)
        return
    for i in range(0,len(s)):
        permutations(s[:i]+s[i+1:],ans+s[i])
c=0
permutations("abc","")
print(c)
'''
# Ex-12:-subsets of the given string
'''def subsets(s,ans,index):
    if index==len(s):
        print(ans)
        return
    subsets(s,ans+s[index],index+1)
    subsets(s,ans,index+1)
subsets("abc","",0)
'''
'''def subsets(s,ans,index):
    if index==len(s):
        if len(ans)==0:
            print("null")
        else:
            print(ans)
        return
    subsets(s,ans+s[index],index+1)
    subsets(s,ans,index+1)
subsets("abc","",0)
'''
# ex-13:-Tower of Hanoi
'''def towers(n,src,temp,dest):
    if n==1:
        print(f"move disc {n} from {src} to {dest}")
    else:
        towers(n-1,src,dest,temp)
        print(f"move disc {n} from {src} to {dest}")
        towers(n-1,temp,src,dest)
n=int(input("enter a no of disc:"))
towers(n,"src","temp","dest")
'''
# Chapter-08:-Backtracking
# ==================
# using recursion
'''def change(l,index,value):
    if index==len(l):
        return
    # l[index]=value
    change(l,index+1,value+1)
l=[0,0,0,0,0]
print(l)
change(l,0,1)
print(l)
'''

# using backtracking
'''def change(l,index,value):
    if index==len(l):
        print(l)
        return 
    l[index]=value
    change(l,index+1,value+1)
    l[index]=l[index]-2
l=[0,0,0,0,0]
print(l)
change(l,0,1)
print(l)
'''
# class-34
# ==========
'''n=4
board=[["X" for i in range(4)] for i in range(4)]
print(board)
'''
'''def printboard(board):
    print("----------chessbord--------")
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=" ")
        print()
    print("----------------------------")
n=4
board=[["X" for i in range(n)] for i in range(n)]
printboard(board)     
'''
# N-Queens_problem
# ----------------------
'''def issafe(board,row,col):
    # vertical up
    # diagonal left up
    # digonal right up

    # vertical up
    i=row-1
    while i>=0:
        if board[i][col]=='Q':
            return False
        i=i-1
    # digonal right up
    i=row-1
    j=col+1
    while i>=0 and j<len(board):
        if board[i][j]=="Q":
            return False
        i=i-1
        j=j+1
    # digonal left up
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]=="Q":
            return False
        i=i-1
        j=j-1
    return True
def nqueens(board,row):
    if row==len(board):
        global c
        c=c+1
        printboard(board)
        return 
    for j in range(len(board)):
        if issafe(board,row,j):
            board[row][j]="Q"
            nqueens(board,row+1)
            board[row][j]="X"
            
def printboard(board):
    print("--------chessboard---------")
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=" ")
        print()
    print("--------------------------------------")
n=4
c=0
board=[["X" for i in range(n)] for j in range(n)]
nqueens(board,0)
print("no of solutions:",c)
'''
# Class-35
# =======
# Grid Ways
'''def gridways(i,j,m,n):
    if i==m-1 and j==n-1:
        return 1
    if i==m or j==n:
        return 0
    val1=gridways(i+1,j,m,n)
    val2=gridways(i,j+1,m,n)
    return val1+val2
m=3
n=3
print(gridways(0,0,m,n))
'''
# suduko problem
# ----------------------
'''def issafe(sudoku,row,col,d):
    # case-1:- row
    for i in range(0,9):
        if sudoku[i][col]==d:
            return False
    # case-2:- col
    for j in range(0,9):
        if sudoku[row][j]==d:
            return False
    # case-3:- grid
    sr=(row//3)*3
    sc=(col//3)*3
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if sudoku[i][j]==d:
                return False
    return True
def sudokusolver(sudoku,row,col):
    if row==9 and col==0:
        return True
    nextrow=row
    nextcol=col+1
    if col+1==9:
        nextrow=row+1
        nextcol=0
    if sudoku[row][col]!=0:
        return sudokusolver(sudoku,nextrow,nextcol)
    for d in range(1,10):
        if issafe(sudoku,row,col,d):
            sudoku[row][col]=d
            if sudokusolver(sudoku,nextrow,nextcol):
                return True
            sudoku[row][col]=0
    return False
def printsuduko(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            print(sudoku[i][j],end=" ")
        print()
sudoku=[[0,0,0,0,6,8,0,0,3],
        [6,0,0,1,9,7,2,5,0],
        [9,0,5,3,0,0,6,8,7],
        [0,5,0,0,0,3,8,9,0],
        [3,0,0,8,0,0,0,0,0],
        [0,0,0,9,0,6,3,4,0],
        [0,3,0,6,8,0,0,0,9],
        [5,0,0,7,3,0,1,0,2],
        [7,0,4,2,1,0,0,0,0]]
printsuduko(sudoku)
if sudokusolver(sudoku,0,0):
    print("solution existed")
    printsuduko(sudoku)
else:
    print("solution not existed")
'''
# class-36
# =========
# Chapter-09:-Dynamic Programming
# -----------------------------------------
# Applications 1--> fibonacci number
# --------------------------------------------
# Implementation of fabonacci sequence with recursion
'''def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(6))
'''
'''def fib(n):
    global c
    c+=1
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
c=0
print(fib(6))
print(f"no of calculations:{c}")
'''
# Implementation of fib seq with memorization
'''l=[None]*7
def fib(n):
    global c
    c=c+1
    if l[n]!=None:
        return l[n]
    if n==0 or n==1:
        l[n]=n
    else:
        l[n]=fib(n-1)+fib(n-2)
    return l[n]
c=0
print(fib(6))
print(f"no of calculations :{c}")
'''
# Implementation of fib seq with tabulation
'''def fib(n):
    dp=[None]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[n]
print(fib(6))
'''
# class-37
# ======
# Application-2:-climbing stairs
# ---------------------------------
# count no of  ways  to reach nth stairs,the person can climb either 1 or 2 steps at a time
'''def countways(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return countways(n-1)+countways(n-2)
for i in range(5):
    print(f"no of steps:{i} and sum of ways to reach top:{countways(i)}")
'''
'''def countways(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    for i in range(1,n+1):
        if i==1:
            dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(countways(9))
for i in range(10):
    print(f"{i}===>{countways(i)}")
'''
# Application:- Knapsack Problem
# -----------------------------------
'''def knap(w,wts,vals,n):
    if w==0 or n==0:
        return 0
    if wts[n-1]>w:
        return knap(w,wts,vals,n-1)
    return max(vals[n-1]+knap(w-wts[n-1],wts,vals,n-1),knap(w,wts,vals,n-1))
w=10
wts=[5,4,6,3]
vals=[10,40,30,50]
n=4
print(knap(w,wts,vals,n))
'''
# class-38
# ===========
# Dynamic programming solution for knapsack problem
'''def knapsack (w,wts,vals,n):
    dp=[[0 for i in range(w+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wts[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-wts[i-1]]+vals[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][w]
w=10
wts=[5,4,6,3]
vals=[10,40,30,50]
n=4
print(knapsack(w,wts,vals,n))
'''
# class-39
# ===========
# chapter-10
# --------------
# ex-1: read and write string
'''s=input("enter a string:")
print(s)
'''
# ex-2:-read string and print characters present at +ve and -ve locations
'''s=input("enter a string:")
index1=0
index2=-1
while index1<len(s) and index2>-(len(s)+1):
    print(f"index={index1} value={s[index1]} index={index2} value={s[index2]}")
    index1+=1
    index2-=1
'''
# ex3:-print characters present at even index values
'''s=input("enter a string:")
index=0
while index<len(s):
    if index%2==0:
        print(f"index={index} and char={s[index]}")
    index+=1
'''
# ex-4: print characters present at odd index
'''s=input("enter a string:")
index=0
while index<len(s):
    if index%2!=0:
        print(f"index={index} and char={s[index]}")
    index+=1
'''
# ex-5: count no of vowels present in string
'''import re
def fun(s):
    l=re.findall("[aeiou]",s)
    return len(l)
s=input("enter a string:")
print(fun(s))
'''
# ex-6:-
# count no of consonants present in a string
'''import re
def fun(s):
    if s.isalpha():
        return len(re.findall("[^aeiou]",s))
s=input("enter a string:")
print(fun(s))
'''
# ex:-7- count no of alphabets
'''import re
def fun(s):
    return len(re.findall("[a-z A-Z]",s))
s=input("enter a string:")
print(fun(s))
'''
# ex-8:-count no of digits
'''import re
def fun(s):
    return len(re.findall("[0-9]",s))
s=input("enter  a string:")
print(fun(s))
'''
# ex:9-count spaces
'''import re
def fun(s):
    return len(re.findall("[ ]",s))
s=input("enter a string:")
print(fun(s))
'''
# ex:10-count special characters
'''import re
def fun(s):
    return len(re.findall("[^a-z A-Z 0-9 ]",s))
s=input("enter  a string:")
print(fun(s))
'''
# ex:11-reverse a given string
'''def fun(s):
    res=""
    for i in s:
        res=i+res
    return res
s=input("enter a number:")
print(fun(s))
'''
# ex:12- convert a given string into upper case
'''def fun1(s):
    return s.upper()
def fun2(s):
    res=""
    for i in s:
        if i.islower():
            res=res+chr(ord(i)-32)
        else:
            res=res+i
    return res
s=input("enter a string:")
print(fun1(s))
print(fun2(s))
'''
# ex:13- convert given string into lower case
'''def fun(s):
    res=""
    for i in s:
        if i.isupper():
            res=res+chr(ord(i)+32)
        else:
            res=res+i
    return res
s=input("enter  a string:")
print(fun(s))
'''
# ex:14-taggle case or swap case
'''def fun1(s):
    return s.swapcase()
def fun2(s):
    res=""
    for i in s:
        if i.isupper():
            res=res+chr(ord(i)+32)
        if i.islower():
            res=res+chr(ord(i)-32)
    return res
s=input("enter  a string:")
print(fun1(s))
print(fun2(s))
'''
# ex-15: convert even index character into upper case odd indexed char into lower case
'''def fun(s):
    res=""
    for i in range(len(s)):
        if i%2==0:
            res=res+s[i].upper()
        else:
            res=res+s[i].lower()
    return res
s=input("enter a string:")
print(fun(s))
'''
# ex-16: reverse the senetnce
'''def fun(s):
    return s[::-1]
def fun1(s):
    res=""
    for i in s:
        res=i+res
    return res
s=input("enter a sentence:")
print(fun(s))
print(fun1(s))
'''
# ex:17- reverse the even indexed words in sentence
'''def fun(s):
    l=[]
    index=0
    for i in s.split():
        if index%2==0:
            l.append(i[::-1])
        else:
            l.append(i)
        index+=1
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# ex-18: reverse the odd index words in sentence
'''def fun(s):
    l=[]
    index=0
    for i in s.split():
        if index%2!=0:
            l.append(i[::-1])
        else:
            l.append(i)
        index+=1
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# ex:19-reverse individual words in sentence
'''def fun(s):
    l=[]
    for i in s.split():
        l.append(i[::-1])
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# ex:20-convert each word first char into upper case
'''def fun(s):
    l=[]
    for i in s.split():
        l.append(i[0].upper()+i[1:].lower())
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# ex:21-convert each word first and last char into upper case
'''def fun(s):
    l=[]
    for i in s.split():
        if len(i)!=1:
            l.append(i[0].upper()+i[1:len(i)-1].lower()+i[-1].upper())
        else:
            l.append(i[0].upper())
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# ex-22: convert every word into upper case except frist and last char
'''def fun(s):
    l=[]
    for i in s.split():
        if len(i)!=1:
            l.append(i[0].lower()+i[1:len(i)-1].upper()+i[-1].lower())
        else:
            l.append(i[0].lower())
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# ex-23: convert every even length words into upper case remaining lower case
'''def fun(s):
    l=[]
    for i in s.split():
        if len(i)%2==0:
            l.append(i.upper())
        else:
            l.append(i.lower())
    return " ".join(l)
s=input("enter a sentence:")
print(fun(s))
'''
# class-40
# ======
# ex-24:return middle char from a string
'''def fun(s):
    if len(s)%2!=0:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]
s=input("enter a string:")
print(fun(s))
'''
# ex-25: sort the string i.e characters present in the string
# ex:-bacd--->abcd
'''def fun(s):
    l=list(s)
    l.sort()
    return "".join(l)
print(fun("bacd"))
print(fun("prakash"))
'''
# ex-26: sort the names
'''def fun(l):
    l.sort()
def fun1(l):
    return l.sort()
l=["ijk","xyz","pqrs","abc"]
fun(l)
print(l)
fun1(l)
print(l)
'''
# ex:27-remove duplicate character
'''def fun(s):
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    return "".join(l)
s="abca"
print(fun(s))
'''
# ex:28-remove special characters
'''import re
def fun(s):
    return re.sub("[^a-z A-Z 0-9 ]","",s)
s=input("enter a string:")
print(fun(s))
'''
# ex:29-remove vowels from a string
'''import re
def fun(s):
    return re.sub("[aeiou]"," ",s)
s=input("enter a string:")
print(fun(s))
'''
# ex:30-check a string is palindrome or not
'''def fun(s):
    low=0
    high=len(s)-1
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True
print(fun("abba"))
'''
# ex:31-return longest (length) palindrome in a string
'''def fun1(s):
    low=0
    high=len(s)-1
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True
def fun2(s):
    return len(s)
def fun(s):
    l=[]
    for i in s.split():
        if fun1(i):
            l.append(i)
    l.sort(key=fun2,reverse=True)
    print(l)
    return l[0]
print(fun("a abc aba madam sir malayalam liril prakash"))
print(fun("a ab abc madam sir liril prakash"))
print(fun("a b aaaaaa abc aba madam sir liril prakash"))
'''
# ex-32:check if a string is rotated
'''def fun(s1,s2):
    if len(s1)!=len(s2):
        return False
    temp=s1+s1
    return temp.find(s2)!=-1
print(fun("abcd","cdab"))
print(fun("abcd","cdba"))
print(fun("ABAAA","BAAAA"))
'''
# ex-33: check two strigs are anagrams or not
'''def fun(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return s1==s2
print(fun("listen","silent"))
print(fun("abcd","cadb"))
print(fun("abc","abd"))
'''
# ex:34-pangram 
# panram means eachina sentence lo a-z(all alphabets) all leeters cover avalli it is pangram
'''def fun(s):
    for i in range(97,123):
        if chr(i) not in s:
            return False
    return True
print(fun("the quick brown fox jumps over the lazy dog"))
print(fun("the quick brown fox jumps over the lay dog"))
'''
# ex-35:-string validation
# given a string representing a password. you need to check if the string is valid or not. A valid string has the following properties
# i. length greater than or equal to 8
# 2.contai  at least 1 numeric character   
# 3.contain at least 1 upper case and lower case character
# 4. contain at least 1 special character @#!$_*
'''def fun(s):
    if len(s)>=8:
        if any(ch.isdigit() for ch in s):
            if any(ch.islower() for ch in s):
                if any(ch.isupper() for ch in s):
                    if any(not ch.isalnum() and not ch.isspace() for ch in s):
                        return "valid string"
    return "not valid string"
s=input("enter a password:")
print(fun(s))
'''
