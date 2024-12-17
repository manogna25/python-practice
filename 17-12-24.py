'''l=[int(i) for i in input("enter the list of numbers seperated by space: ").split(" ")]
for i in l:
    if i==0:
        l.remove(i)
        a=0
        l.append(a)
print(l)'''
#matrix
'''l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1)
for i in l1:
    print(i)
for i in l1:'''
'''n=int(input("size:"))
m1=[]
for i in range(n):
    v=[]
    for j in range(n):
        v.append(0)
    m1.append(v)
for i in m1:
    print(i)'''
'''n=int(input("size:"))
m1=[]
for i in range(n):
    v=[]
    for j in range(n):
        a=int(input())
        v.append(a)
    m1.append(v)
for i in range(n):
    for j in range(n):
        print(m1[i][j],end=" ")
    print()
'''
'''r,c=list(map(int,input("enter:").split(" ")))
m1=[[int(input()) for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        print(m1[i][j],end=" ")
    print()
'''
'''r,c=list(map(int,input("enter:").split(" ")))
m1=[[int(input()) for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        print(m1[j][i],end=" ")
    print()'''
'''r,c=list(map(int,input("enter:").split(" ")))
m1=[]
c1=1
for i in range(r):
    v=[]
    for j in range(c):
        v.append(c1)
        c1=c1+1
    m1.append(v)
print("matrix:")
for i in range(r):
    for j in range(c):
        print(m1[i][j],end=" ")
    print()
print("Transpose")
for i in range(c):
    for j in range(r):
        print(m1[j][i],end=" ")
    print()'''
#identity matrix
'''r,c=list(map(int,input("enter:").split(" ")))
m1=[]
a=0
if r==c:
    for i in range(r):
        v=[]
        for j in range(c):
            if i==j:
                v.append(1)
            else:
                v.append(a)     
        m1.append(v)
    print("matrix:")
    for i in range(r):
        for j in range(c):
            print(m1[i][j],end=" ")
        print()
else:
    print("it is not square matrix")'''
'''r,c=list(map(int,input("enter:").split(" ")))
m1=[]
for i in range(r):
    v=[]
    a=list(map(int,input("enter ").split(" ")))
    if len(a)==c:
        v.append(a)
        m1.append(v)
    else:
        print("enter correctly")
print("matrix:",m1)
for i in range(r):
    for j in range(c):
        print(m1[i][j],end=" ")
    print()'''
'''n=4
m1=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
print("matrix:")
for i in range(n):
    for j in range(n):
        print(m1[i][j],end=" ")
    print()
'''
#10001
#01010
#00100
#01010
#10001
'''n=7
m1=[[1 if (i==j or j==n-i-1) else 0 for j in range(n)] for i in range(n)]
print("matrix:")
for i in range(n):
    for j in range(n):
        print(m1[i][j],end=" ")
    print()
'''
#00100
#01010
#10001
#01010
#00100
'''n=int(input("enter"))
if n%2!=0:
    mid=n//2
    m1=[[1 if (abs(i - mid) + abs(j - mid) == mid) else 0 for j in range(n)] for i in range(n)]
    print("matrix:")
    for i in range(n):
        for j in range(n):
            print(m1[i][j],end=" ")
        print()
else:
    print("enter positive number")
'''
#upper count lower count
'''s=input("enter the string:")
uc=0
lc=0
for i in s:
    if i.isupper():
        uc+=1
    if i.islower():
        lc+=1
    else:
        continue
print("upper count:",uc)
print("lower count:",lc)
'''
#company finding
'''
s=input("enter: ")
a=s.index("@")
b=s.index(".")
print("company name:",s[a+1:b])'''
#pangram
'''s=input("enter:")
t=s.lower()
a="abcdefghijklmnopqrstuvwxyz"
count=0
for i in range(len(s)):
    if s[i] in a:
        count+=1
if count>=26:
    print("s")
else:
    print("n")
'''
#anagram
'''s=input("enter:")
t=input("enter:")
c=0
if len(s)==len(t):
    for i in s:
        if i not in t:
            c=1
    if c==1:
        print("not anagram")
    else:
        print("Anagram")
else:
    print("invalid")
#
s=input("enter:")
t=input("enter:")
if sorted(s)==sorted(t):
    print("anagram")
else:
    print("not anagram")
'''
'''s=input("enter:")
b=s.count("-")
l=""
for i in s:
    if i!="-":
        l=l+i
print(b*"-"+l)
'''
'''s=input("enter:")
b=s.count("-")
for i in s:
    if i=="-":
        s.replace(i,"")
print(b*"-"+l)
'''
s=input("enter your password:")
al=0
n=0
for i in s:
    if i.isupper():
        al+=1
    if i.isdigit():
        n+=1
if len(s)>=4:
    '''if s[0].isnumeric():
        print("bad")
    elif (" " in s) or ("/" in s):
        print("bad")
    elif al==0:
        print("bad")
    elif n==0:
        print("bad")'''
    if s[0].isdigit() or (" " in s) or ("/" in s) or al==0 or n==0:
        print("invalid password format")
    else:
        print("good")
else:
    print("worst")
