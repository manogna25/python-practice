'''s1={1,2,3}
s2={5,6,7,8}
print(set.union(s1,s2))
print(set.intersection(s1,s2))
print(set.difference(s1,s2))
print(set.isdisjoint(s1,s2))
print(set.issubset(s1,s2))
s3=set.copy(s1)
print(sorted(s3))'''
#oops
#Example with constructor
'''class Employee:
    def __init__(self,name,ids,salary):
        self.name=name
        self.ids=ids
        self.salary=salary
    def output(self):
        print("name:",self.name)
        print("id:",self.ids)
        print("salary:",self.salary)
x=Employee("Manu",304,1000000)
x.output()
y=Employee("siva",305,1000000)
y.output()
a=(input("name"))
b=int(input("id"))
c=int(input("salary"))
z=Employee(a,b,c)
z.output()'''
#example without constructor
'''class Employee:
    def details(self,name,ids,salary):
        self.name=name
        self.ids=ids
        self.salary=salary
    def output(self):
        print("name:",self.name)
        print("id:",self.ids)
        print("salary:",self.salary)
x=Employee()
x.details("m",1,1000)
x.output()
'''
'''class Employee:
    pass
x=Employee()
x.a=20
print(x.a)
y=Employee()
y.b=200
print(y.b)'''
#single inheritance
'''class Parent:
    def fun1(self):
        print("hii")
    def fun2(self):
        print("hello")
class Child(Parent):
    def fun3(self):
        print("good morning")
v=Child()
v.fun2()
v.fun3()
v.fun1()
'''
#multiple inheritance
'''class Parent1:
    def fun1(self):
        print("hii")
class Parent2:
    def fun2(self):
        print("hello")
class Child(Parent1,Parent2):
    def fun3(self):
        print("good morning")
v=Child()
v.fun2()
v.fun3()
v.fun1()
'''
#polymorphism
'''class Shape:
    def area(self):
        print("Area")
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print(3.14*self.r*self.r)
class Rect(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
class Square:
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)
s=[Shape(),Circle(3),Rect(5,7),Square(7)]
for i in s:
    i.area()
'''
