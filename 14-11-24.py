#reverse number
'''def rev(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(rev(n//10)))
n=int(input("n:"))
r=rev(n)
print(r)
if r==n:
    print("Palindrome")
else:
    print("not")
'''
'''def reverse(n,rev):
    if n==0:
        return rev
    else:
        return reverse(n//10,rev*10+n%10)
n=int(input("n:"))
rev=0
res=reverse(n,rev)
print(res)
if res==n:
    print("Palindrome")
else:
    print("not")
'''
'''def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2)+fib(n-1)
n=int(input("enter:"))
for i in range(n):
    print(fib(i))'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print(j+1,end="")
    print()
'''
'''n=int(input())
v=1
for i in range(n):
    for j in range(n):
        print(v,end="")
        v+=1
    print()
'''
'''n=int(input("n: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
'''n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
'''
'''n=int(input())
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
'''
'''n=int(input("n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''n=int(input("n:"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
'''
'''n=int(input("n:"))
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(2*n-2*i-1):
        print("*",end="")
    print()
'''
'''n=int(input("n:"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(2*n-2*i-1):
        print("*",end="")
    print()
'''
'''n=int(input("n: "))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(n-i):
        print("*",end="")
    print()
'''
'''n=int(input("enter:"))
for i in range(1,2*n):
    if i<=n:
        start=i
    else:
        start=2*n-i
    print(start*"*",end=" ")
    print()
'''
'''n=int(input("enter:"))
for i in range(1,2*n):
    #for k in range(n-i):
        #print(" ",end="")
    if i<=n:
        start=i
        spaces=n-i
    else:
        start=2*n-i
        spaces=i-n
    #for k in range(i-n):
        #print(" ",end="")
    print(spaces*" ",start*"*",end=" ")
    print()
'''
'''n=int(input("n:"))
for i in range(1,n+1):
    for k in range(n-i):
        print("1",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()
'''
'''n=int(input("n:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    for k in range(n-i):
        print("1",end=" ")
    print()
'''
'''n=int(input())
size=2*n-1
for i in range(size):
    for j in range(size):
        v=n-min(i,j,size-1-i,size-1-j)
        print(v,end=" ")
    print()
'''
'''n=int(input())
v=1
for i in range(n):
    for j in range(i+1):
        print(v,end=" ")
        v+=1
    print()
'''
n=int(input())
for i in range(1,n+1):
    ch='A'
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
