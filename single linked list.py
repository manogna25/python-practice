#sll
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
    def insertatlast(self,x):
        if self.head is None:
            self.insertatfirst(x)
            return
        else:
            newnode=Node(x)
            t=self.head
            while t.next is not None:
                t=t.next
            t.next=newnode
    def deleteatfirst(self):
        if self.head is None:
            print("deletion is not possible")
            return
        else:
            t=self.head
            self.head=self.head.next
            print("data deleted is :",t.data)
    def deleteatlast(self):
        t=self.head
        if self.head is None:
            print("deletion is not possible")
            return
        elif self.head.next is None:
            self.head=None
            print("data deleted is :",t.data)
        else:
            prev=None
            while t.next is not None:
                prev=t
                t=t.next
            prev.next=None
            print("data deleted is :",t.data)
    def search(self,s):
        if self.head is None:
            print("Searching not possible")
        else:
            t=self.head
            while t is not None:
                if t.data==s:
                    print(s,"is found")
                    return
                t=t.next
            else:
                print("Not Found")
    def insertdataafter(self,dataafter,x):
        if self.head is None:
            print("Empty")
            return
        else:
            newnode=Node(x)
            t=self.head
            while t.next is not None and t.data is not dataafter:
                t=t.next
            if t.data is not dataafter:
                print("Not possible")
            elif t.next is not None:
                newnode.next=t.next
                t.next=newnode
            else:
                t.next=newnode
m=SLL()
m.display()
m.insertatfirst(10)
m.display()
m.insertatfirst(20)
m.insertatfirst(30)
m.display()
n=5
for i in range(n):
    a=int(input("enter:"))
    m.insertatfirst(a)
m.display()
m.insertatlast(234)
m.insertatlast(124)
m.display()
m.search(124)
m.deleteatfirst()
m.display()
m.deleteatlast()
m.display()
m.insertdataafter(3,100)
m.display()

