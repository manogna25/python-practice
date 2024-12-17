'''x=int(input("enter no of 5 rupee coins you have:"))
y=int(input("enter no of 10 rupee coins you have:"))
z=int(input("enter amount of each chocolate:"))
w= 5*x + 10* y
n=w//z
print("max no of chocolates:",n)'''
'''n=int(input("enter a number:"))
t=0
temp=n
while n>0:
    r=n%10
    t=t*10+r
    n=n//10
print(t)
if temp==t:
    print("yes")
else:
    print("no")'''
'''def rev(n):
    t=0
    while n>0:
        r=n%10
        t=t*10+r
        n=n//10
    print(t)
n=int(input())
rev(n)'''
#climbing problem
'''def cp(n):
    if n==0 or n==1:
        return 1
    else:
        a,b=1,2
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
        return b
n=int(input("total no of steps:"))
print("no of ways:",cp(n))
'''
'''def cp(n):
    if n==0 or n==1:
        return 1
    else:
        return cp(n-1)+cp(n-2)
n=int(input("enter no of steps:"))
print("total:",cp(n))'''
'''def cp(n):
    if n==0 or n==1:
        return 1
    else:
        d=[0]*(n+1)
        d[0]=1
        d[1]=1
        for i in range(2,n+1):
            d[i]=d[i-1]+d[i-2]
        return d[n]
n=int(input("enter no of steps:"))
print("total:",cp(n))'''
'''def sos(n):
    l=[89,145,42,20,4,16,37,58]
    while True:
        if n==1:
            return "yes"
        if n in l:
            return "no"
        else:
            sum=0
            while n>0:
                r=n%10
                sum+=r**2
                n=n//10
            n=sum
n=int(input("n:"))
print(sos(n))'''
'''n=int(input("enter a num:"))
l1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
r1=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
r=""
i=0
while n>0:
    count=n//l1[i]
    r=r+r1[i]*count
    n=n%l1[i]
    i=i+1
print(r)
'''
n=int(input("enter no of songs in playlist:"))
l=[int(i) for i in input("data:").split(" ")]
i=int(input("enter your fav song position:"))
a=l[i-1]
l.sort()
np=l.index(a)+1
print("new position: ",np)
