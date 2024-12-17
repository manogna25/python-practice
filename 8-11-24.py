'''import math
x=int(input("enter a x value:"))
y=int(input("enter a y value:"))
for n in range(x,y+1):
    if n>1:
        is_prime=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print(n,end=" ")'''
'''str="manogna"
print(len(str))
print(str.capitalize())
str="i am going to the college"
print(str.title())
print(str.replace('going','went'))
print(str.startswith('a'))
print(str.endswith('e'))
print(str.count('i'))
print(str.find('g'))
print(str.index('c'))
print(str[:2])
print(str[2:])
print(str[3:7])
print(str[:-1])
print(str[::-1])
print(str[-1],str[::-2])
print(str[:])
print(str.strip())
print(str.lstrip())
print(str.rstrip())
str=''
print(str.isspace())
a="123"
str="i am going to the college"
print(a.isdigit())
print(a.isalpha())
print(a.isnumeric())
print(str.upper())
print(str.lower())
a=5
b=3
print("a<<2:",a<<2)
s="10010"
c=int(s,2)
print("after converting to integer base 2:",end=" ")
print(c)
print(float(s))
'''
myset={1,2,3}
mydict=dict.fromkeys(myset,0)
print(mydict)
l1=[1,2,3,4]
l2=[1,2,3,4]
d=dict.fromkeys(l1,l2)
print(d)
