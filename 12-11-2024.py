#tuple
'''a=input("enter: ").split()
t1=tuple(a)
print(t1)
t1=(1,"abc",78.9,879,[1,2,3,4],(1,2))
print(t1)
print(t1[4][1])
print(t1[1][2])
t1[4][1]=200
print(t1)
# not possible t1[1][2]="d"
del t1[4][1]
print(t1)'''
#
'''list1=input("data: ").split(",")
print("list:",list1)
mytuple=tuple(list1)
print("tuple:",mytuple)'''
#
'''l=input("data: ").split(",")
print("list:",l)
t=tuple(l)
print("tuple:",t)
index=int(input("index: "))
if index<len(t) and index>=(-len(t)):
    print("element:",t[index])
else:
    print("enter valid index")
'''
#dictionaries
'''d={1:10,2:20,3:30}
print(d)
d1={"a":10,"b":200,"c":300}
print(d1)
d1={"a":10,500:200,"c":300}
print(d1)
print(d.keys())
print(d.values())
print(sorted(d.items()))
for i,j in sorted(d.items()):
    print(i,"->",j)
'''
#using []
'''d[2]="hello"
print(d)
d[1]="hii"
print(d)'''
#using get()
'''d={1:5,2:10,3:15,4:20}
print(d.get(3))
d.pop(2)
print(d)'''
#indirect input 1
'''k=input("keys:").split(",")
v=input("values:").split(",")
d=dict(zip(k,v))
print(d)
print(sorted(d.items()))
for i,j in sorted(d.items()):
    print(i,j)
'''
#indirect input 2
'''k=input("keys:").split(",")
v=input("values:").split(",")
d={}
for i in range(len(v)):
    d[k[i]]=v[i]
print(d)
print(sorted(d.items()))'''
#update()
'''d1={1:2,2:3,4:5}
d2={6:5,7:4}
d1.update(d2)
print(d1)
#clear()
d2.clear()
print(d2)
print(len(d1))'''
#copy
'''
d1={1:2,2:3}
d2=d1.copy()
print(d1,d2)
'''
#set()
'''l=input("set: ").split(",")
s=set(l)
print(sorted(s),type(s))
k="hii"
s.add(k)
print(sorted(s))
l2=["1","2","4"]
s.update(l2)
print(sorted(s))
'''
'''s={1,2,3,4,5}
k=5
s.discard(k)
print(sorted(s))
l=2
s.remove(l)
print(sorted(s))'''
#Recursive functions
#sum of n natural numbers
'''def s(n):
    if n==1:
        return n
    else:
        return n+s(n-1)
n=int(input("n:"))
print(s(n))'''
#factoria
'''def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
n=int(input("n:"))
print(f(n))'''
#palindrome
'''def p(s):
    k=len(s)
    if k<=1:
        return 1
    else:
        if s[0]==s[-1]:
            return p(s[1:-1])
        else:
            return 0
s=input("s:")
if p(s)==1:
    print("Palindrome")
else:
    print("not a palindrome")'''
#reverse number
def rev(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(rev(n//10)))
n=int(input("n:"))
print(rev(n))
    
