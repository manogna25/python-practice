class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circularqueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isempty(self):
        return self.front is None
    def enqueue(self,data):
        newnode=Node(data)
        if self.isempty():
            self.front=newnode
            self.rear=newnode
            self.rear.next=self.front
        else:
            self.rear.next=newnode
            self.rear=newnode
            self.rear.next=self.front
        print(f"Enqueue:{data}")
    def dequeue(self):
        if self.isempty():
            prit("empty")
            return None
        data=self.front.data
        if self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.rear.next=self.front
        print(f"Dequeue:{data}")
        return data
    def peek(self):
        if self.isempty():
            print("--------empty-------")
            return None
        print(self.front.data)
    def display(self):
        if self.isempty():
            print("------empty------")
            return None
        t=self.front
        print("Queue element are:")
        while True:
            print(t.data,end=" ")
            t=t.next
            if t==self.front:
                break
        print()
m=Circularqueue()
while 1:
    op=int(input("Choose from below\n 1.Enqueue \n 2.Dequeue\n3.Display\n4.peek\n5.Exit\n"))
    if op==1:
        n=int(input("enter value to enqueue:"))
        m.enqueue(n)
    elif op==2:
        m.dequeue()
    elif op==3:
        m.display()
    elif op==4:
        m.peek()
    else:
        break
