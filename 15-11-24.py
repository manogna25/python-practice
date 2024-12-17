'''s=input("enter:")
s1=""
c=0
for i in s:
    if i!= " ":
        s1=s1+i
    else:
        c=c+1
print(s1)
print(c)'''
'''s=input("enter")
l=s.split(" ")
o=l[::-1]
for i in o:
    print(i,end=" ")
'''
'''s=input()
a=s.title()
print(a)'''
s=input("enter:")
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
