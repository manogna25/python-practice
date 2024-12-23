#CsLL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            t=self.head
            print(t.data,end=" ")
            while t.next != self.head:
                t=t.next
                print(t.data,end=" ")
            print()
    def insertatfirst(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
        else:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=self.head
    def deleteatfirst(self):
        t=self.head
        if self.head is None:
            print("Deletion not possible")
            return
        elif self.head is self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
        print("Deleted node:",t.data)
    def insertatlast(self,data):
        newnode=Node(data)
        if self.head is None:
            self.insertatfirst(data)
            return
        else:
            '''t=self.head
            while t.next is not self.head:
                t=t.next
            t.next=newnode
            self.tail=newnode
            newnode.next=self.head'''
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
    def deleteatlast(self):
        t=self.head
        if self.head is None:
            print("deletion is not possible")
            return
        elif self.head is self.tail:
            self.head=self.head.next
            self.tail.next=self.head
        else:
            p=None
            while t.next is not self.head:
                p=t
                t=t.next
            t.next=None
            p.next=self.head
            self.tail=p
        print("Deleted node:",t.data)
    def search(self,x):
        if self.head is None:
            print("searching not possible")
            return
        else:
            t=self.head
            while t.next is not self.head:
                if t.data==x:
                    print(x,'is found')
                    return
                t=t.next
            if t.next is self.head and t.data==x:
                print(x,"found")
            else:
                print("search element not found")
    def insertafterposition(self,after,data):
        newnode=Node(data)
        if self.head is None:
            self.insertatfirst(data)
            return
        else:
            t=self.head
            while t.data!=after:
                t=t.next
            newnode.next=t.next.next
            t.next=newnode
    '''def deleteafterposition(self,after):
        if self.head is None:
            print("Deletion is not possible")
            return
        else:
            t=t.head
            while '''
m=CSLL()
m.display()
m.insertatfirst(23)
m.insertatfirst(44)
m.display()
m.deleteatfirst()
m.deleteatfirst()
m.display()
m.insertatfirst(323)
m.insertatfirst(45)
m.insertatfirst(1)
m.display()
m.insertatlast(234)
m.insertatlast(43333)
m.insertatlast(2)
m.display()
m.deleteatlast()
m.display()
m.search(1)
m.insertafterposition(45,10)
m.display()
m.search(43333)
