'''l=list(map(int,input("enter:").split(",")))
e=int(input("enter a element to search:"))
print(e in l)
'''
'''l=[int(i) for i in input("enter:").split(",")]
e=int(input("enter a element to search:"))
print(e in l)
'''
'''l=[int(i) for i in input("enter:").split(",")]
e=int(input("enter a element to search:"))
a=l.index(e)
print("index of search element:",a)'''
#linear search
'''a=input("enter:").split(",")
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
e=int(input("enter a element:"))
for i in a:
    if i==e:
        print("found")
        break
else:
    print("not found")
'''
#sorted()
'''l=[5,4,3,2,1]
print(l)
l2=sorted(l)
print(l)
print(l2)'''
#.sort()
'''l1=[34,23,4,32]
print(l1)
l1.sort()
print(l1)'''
#sorting methods
#bubble sort
'''l=[int(i) for i in input("enter:").split(",")]
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        
print(l)
'''
#binary search
'''l=[int(i) for i in input("enter:").split(",")]
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
s=int(input("enter element to search:"))
left=0
right=len(l)-1
while left<=right:
    mid=(left+right)//2
    if l[mid]==s:
        print("found")
        break
    elif l[mid]<s:
        left=mid+1
    else:
        right=mid-1
else:
    print("not found")
'''
#SINGLY LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.lastnode=None
    def insertatfirst(self,x):
        newnode=Node(x)
        newnode.next=self.head
        self.head=newnode
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            t=self.head
            while t is not None:
                print(t.data,end=" ")
                t=t.next
            print()
m=SLL()
m.display()
m.insertatfirst(10)
m.insertatfirst(20)
m.insertatfirst(30)
m.display()
n=5
for i in range(n):
    a=int(input("enter:"))
    m.insertatfirst(a)
m.display()
