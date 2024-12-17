'''str=input("str: ")
a=str.upper()
l1=[]
for i in a:
    if i not in l1:
        print(i,a.count(i))
        l1.append(i)'''
'''str=input("str: ")
num=int(input("num: "))
l=len(str)
if num>=0 and num<l:
    print(str[:num]+str[num+1:])
    #print(str.replace(str[num],""))
else:
    print("num +ve and less than len of string")
'''
'''s=input("enter: ").split(" ")
print(s)
for i in range(len(s)):
    s[i]=int(s[i])
print(s)'''
'''n=int(input("enter:"))
l1=[]
for i in range(n):
    a=int(input("enter: "))
    l1.append(a)
print("list: ",l1)'''
'''l1=[i for i in range(1,11)]
print(l1)
l2=[int(input()) for i in range(1,4)]
print(l2)'''
#s="botlle"
#s="123456"
'''s=input("enter")
l1=[int(i) for i in s]
print(l1)
s=input("enterr: ").split(" ")
l1=[int(i) for i in s]
print(l1)
l1=[int(i) for i in input()]
print(l1)'''
'''l1=[i for i in range(1,10) if i%5==0]
print(l1)
l2=["even" if int(i)%2==0 else "odd" for i in input("enter").split()]
print(l2)
l3=["positive" if int(i)>0 else "negative" for i in input("enter:").split()]
print(l3)'''
#l1=map(i,int(input("Enter:")))
#l1=map(i,int(input("enter:")).split(" "))
#l1,l2=list(map(int,input("enter:").split(" ")))
#print(l1,l2)
'''l1=[1,2,3,4,5]
l2=[6,5,4,3,2,1]
print(10 in l1)
print(10 not in l2)
print(l1+l2)
print(l1*3)
print(l1==l2)
print(l1[3])
l3=[32,323,33,[33,3,"hello","namaste"],3]
print(l3[3][1])
print(l3[1:4])
print(l3[3][3][2])
l3[3][2]="c"
print(l3)
l3[3][3]="python"
print(l3)
l1=['10',2,3,4,5]
l1.index(4)
print(l1)
l1.append(11)
l1.insert(0,1)
print(l1)
l1.extend([1,2,3])
print(l1)
l1.reverse()
print(l1)
l2=[1,2,3,42331,33131,0]
l2.sort()
print(l2)
l2.sort(key=None,reverse=True)
print(l2)
'''
'''l1=list(map(int,input("l1: ").split(",")))
l2=list(map(int,input("l2: ").split(",")))
l3=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
        a=abs(l1[i]-l2[i])
        l3.append(a)
    print(l3)
else:
    print("list are different lenghts")
a=[100,23,32]
print(a*0)
'''
#functions
'''def wish():
    print("hello")
def w():
    print("good")
def fun1():
    return "hi"
print(fun1())
wish()
print("hii")
wish()
w()'''
'''def hello():
    print("Good morning")
    print("hello")
    print("hi")
def hii():
    return "c","python","jav"
print(hii())
hello()
print(hii())'''
'''def add():
    """function is for addition"""
    a,b=10,20
    print(a+b)
add()
print(add.__doc__)'''
'''def add(a,b):
    print(a+b)
a=int(input())
b=int(input())
add(a,b)'''
#positional arguments
'''def sub(d,c):
    print(d-c)
a=int(input("a:"))
b=int(input("b:"))
sub(a,b)
sub(87,45)
sub(45,87)'''
#keyword arguments
'''def sub(d,c):
    print(d-c)
a=int(input("a:"))
b=int(input("b:"))
sub(d=a,c=b)
sub(c=b,d=a)'''
#default arguments
'''def sub(d,c=100):
    print(d-c)
a=int(input("a:"))
b=int(input("b:"))
sub(a,b)
sub(a)'''
'''def fun1(n="padma",a=100):
    print(n,a)
fun1("Manogna",25)
fun1()
fun1("Manu")
fun1(a=25)
'''
'''def natural(n):
    print((n*(n+1)//2))
n=int(input("n:"))
natural(n)
def fact(n):
    fact,i=1,1
    if n==0 or n==1:
        print(1)
    else:
        while i<=n:
            fact=fact*i
            i+=1
    print(fact)
a=int(input("a:"))
fact(a)'''
'''s=lambda a,b,c:a+b+c
a,b,c=12,2,2
print(s(a,b,c))
print(s(10,20,30))'''
'''str1=input("str1: ")
c1,c2=input("c1,c2: ").split(" ")
if c1 in str1:
    
    print(str1.replace(c1,c2))
else:
    print("not possible")'''
'''s=input().strip()
c1=input().strip()
s2=""
if c1 in s:
    for i in s:
        if i !=c1:
            s2=s2+i
    print(s2)
'''
x=True
y=0.99
print(y<=x)
x=6
y=3
print(x/y)
x=2
y=2.0
print(x==y)
print(x!=y)

