a="welcomeevbfefveeevevev"
#find,rfind,index,rindex
'''print(a.find('e'))
print(a.find('e',2))
print(a.rfind('e'))
print(a.find('come'))
print(a.find('welcome'))
print(a.find('1'))
print(a.find('a'))
print(a.rindex('e'))
#print(a.index('a'))
'''
#count
'''print(a.count('e'))
print(a.count('f'))
print(a.count('com'))
print(a.count('ve'))
print(a.count(' '))
'''
#replace
'''temp=a.replace('wel','lev')
print(temp)
print(a.replace('wel',' '))
print(a)
b=a.replace('e','w',1)
print(b)
'''
#split
'''a='str ing'
b=a.split(' ')
print(a)
print(b)
a='mo:98765 43210,ro:1234 567'
print(a.split())
print(a.split(','))
print(a.split('-'))
s='siva@gmail.com'
t=s.split('@')
print(t[1])
'''
#join
'''j="zxc"
i="123"
print(i.join(j))
print(j.join(i))
'''
#password checker
'''
a=input("enter the password:")
l=False
u=False
d=False
if len(a)>=8:
    for i in a:
        if i.islower():
            l=True
        elif i.isupper():
            u=True
        elif i.isdigit():
            d=True
        else:
            flag=False
if l and u and d:
    print("Strong")
else:
    print("Weak and try again")
'''
fname=input("First name:")
lname=input("Last name:")
print(fname.capitalize()+" "+lname.capitalize())

