#DLL
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        self.lastnode=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            t=self.head
            while t is not None:
                print(t.data,end=" ")
                t=t.next
            print()
    def insertatfirst(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def deleteatfirst(self):
        if self.head is None:
            print("deletion not posssible")
            return
        else:
            t=self.head
            self.head=self.head.next
            self.head.prev=None
            print("deleted data is ",t.data)
    def insertatlast(self,data):
        if self.head is None:
            self.insertatfirst(data)
            return
        else:
            newnode=Node(data)
            t=self.head
            while t.next is not None:
                t=t.next
            t.next=newnode
            newnode.prev=t
    def deleteatlast(self):
        if self.head is None:
            print("deletion not possible")
            return
        else:
            t=self.head
            while t.next is not None:
                p=t
                t=t.next
            t.prev=None
            p.next=None
            print("deleted element is:",t.data)
    def search(self,s):
        if self.head is None:
            print("searchng not possible")
            return
        else:
            t=self.head
            while t is not None:
                if t.data==s:
                    print(s,"is found")
                    return
                t=t.next
            else:
                print("not found")
m=DLL()
m.display()
m.insertatfirst(22)
m.insertatfirst(233)
m.display()
for i in range(5):
    a=int(input("enter:"))
    m.insertatfirst(a)
m.display()
m.deleteatfirst()
m.display()
m.insertatlast(122)
m.display()
m.deleteatlast()
m.display()
m.search(2)
