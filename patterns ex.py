'''n=int(input())
m=int(input())
for i in range(n):
    print(" "*(i%m),end="")
    for j in range(1,m+1):
        print(j,end=" ")
    print()
for i in range(n-2,-1,-1):
    print(" "*(i%m),end="")
    for j in range(1,m+):
        print(j,end=" ")
    print()
'''
'''n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
'''n=int(input())
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(2*n-2*i-1):
        print("*",end=" ")
    print()
'''
'''n=7
m1=[[1 if (i==j or j==n-i-1) else " " for j in range(n)] for i in range(n)]
print("matrix:")
for i in range(n):
    for j in range(n):
        print(m1[i][j],end=" ")
    print()'''
'''n=int(input("enter"))
if n%2!=0:
    mid=n//2
    m1=[[1 if (abs(i - mid) + abs(j - mid) == mid)  else "" for j in range(n)] for i in range(n)]
    print("matrix:")
    for i in range(n):
        for j in range(n):
            print(m1[i][j],end=" ")
        print()
else:
    print("enter positive number")
'''
'''n=int(input("enter"))
if n%2!=0:
    mid=n//2
    m1=[[1 if (abs(i - mid) + abs(j - mid) == mid) or   else "" for j in range(n)] for i in range(n)]
    print("matrix:")
    for i in range(n):
        for j in range(n):
            print(m1[i][j],end=" ")
        print()
else:
    print("enter positive number")
'''
'''n=int(input("enter:"))
c=0
for i in range(1,n+1):
    for k in range(2*(n-i)):
        print(" ",end="")
    for j in range(2*i-1):
        
        if j<i:
            c+=1
        else:
            c-=1
        print(c,end=" ")
    print()
'''
'''n=int(input())
for i in range(1,n+1):
    c=i
    for k in range(2*(n-i)):
        print(" ",end="")
    for j in range(1,2*i):
        print(c,end=" ")
        if j<i:
            c+=1
        else:
            c-=1
    print()
'''
#room number as alphabetic code
#1-A 2-B .....27-AA 28-AB........52-AZ 53-BA
n=int(input("Room number:"))
result=[]
n=n-1
while n>=0:
    r=n%26
    result.append(chr(r+ord('A')))
    n=n//26-1
result.reverse()
for i in result:
    print(i,end="")
