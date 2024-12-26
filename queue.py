'''queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
front_element=queue.pop(0)
print(front_element)
front_element=queue[0]
print(front_element)
rear_element=queue[-1]
print(rear_element)
isempty=len(queue)==0
print(isempty)
size=len(queue)
print(size)
'''
'''queue=[]
def enqueue():
    n=int(input("enter the value to be inserted into the queue:"))
    queue.append(n)
    display()
    print("------------")
def dequeue():
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue[0],"is deleted")
        queue.pop(0)
        print("-----------")
def display():
    if len(queue)==0:
        print("queue is empty")
        print("-----------")
    else:
        print("Elements in the queue are:")
        for element in queue:
            print(element)
        print("front:",queue[0])
        print("rear:",queue[-1])
while 1:
    op=int(input("Choose from below\n 1.Enqueue \n 2.Dequeue \n3.Display\n4.Exit\n"))
    if op==1:
        enqueue()
    elif op==2:
        dequeue()
    elif op==3:
        display()
    else:
        break
'''
'''max_size=5
queue=[]
def enqueue(queue,max_size,data):
    if len(queue)>=max_size:
        print("queue is overflow")
    else:
        queue.append(data)
        print(f"Enqueue:{data}")
    print("-------")
def dequeue(queue):
    if len(queue)==0:
        print("queue is empty")
    else:
        data=queue.pop(0)
        print(f"Dequeue:{data}")
        print("-----------")
def display(queue):
    if len(queue)==0:
        print("queue is empty")
        print("-----------")
    else:
        print("Elements in the queue are:",queue)
        print("front:",queue[0])
        print("rear:",queue[-1])
while 1:
    op=int(input("Choose from below\n 1.Enqueue \n 2.Dequeue \n3.Display\n4.Exit\n"))
    if op==1:
        n=int(input("enter:"))
        enqueue(queue,max_size,n)
    elif op==2:
        dequeue(queue)
    elif op==3:
        display(queue)
    else:
        break
'''
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self):
        data=int(input("Enter the data to insert: "))
        newnode=Node(data)
        if self.front is None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        if self.front is None:
            print("dequeue not possible")
        elif self.front.next is None:
            print("Popped element:",self.front.data)
            print("-----------")
            self.front=None
        else:
            t=self.front
            print("Popped element:",self.front.data)
            print("-----------")
            self.front=t.next
            t=None
    def display(self):
        if self.front is None:
            print("queue is not possible")
            print("----------")
        else:
            print("elements are:")
            t=self.front
            while t:
                print(t.data,end=" ")
                t=t.next
            print("\nFront:",self.front.data)
            print("Rear:",self.rear.data)
m=Queue()
while 1:
    op=int(input("Choose from below\n 1.Enqueue \n 2.Dequeue \n3.Display\n4.Exit\n"))
    if op==1:
        m.enqueue()
    elif op==2:
        m.dequeue()
    elif op==3:
        m.display()
    else:
        break
m.enqueue()
m.enqueue()
m.enqueue()
m.enqueue()
m.display()
m.dequeue()
m.display()'''
'''stack1=[]
stack2=[]
def enqueue(data):
    stack1.append(data)
    print(f"enqueue:{data}")
def dequeue():
    if len(stack2)==0:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        print("Empty")
        return None
    else:
        return stack2.pop()
def peek():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        print("Empty")
        return None
    else:
        return stack2[-1]
def is_empty():
    return not stack1 and not stack2
def display():
    if is_empty():
        print("Queue us empty")
    else:
        print("Queue elements:",end="")
        for i in stack1:
            print(i,end=" ")
        for i in stack2[::-1]:
            print(i,end=" ")
        print("\n------------")
while 1:
    op=int(input("Choose from below\n1.Enqueue \n2.Dequeue \n3.Display\n4.Peek\n5.exit\n"))
    if op==1:
        n=int(input("enter:"))
        enqueue(n)
    elif op==2:
        r=dequeue()
        if r is not None:
            print(f"Dequeue:{r}")
    elif op==3:
        display()
    elif op==4:
        r=peek()
        if r is not None:
            print(f"Top:{r}")
    else:
        print("exiting...........")
        break
'''
class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def is_full(self):
        return(self.rear+1==self.size and self.front==0)or(self.rear+1==self.front)
        #return (self.rear+1)%self.size==self.front
    def is_empty(self):
        return self.front==-1
    def enqueue(self,item):
        if self.is_full():
            print("Queue id overflow")
            return
        if self.is_empty():
            self.front=0
        if self.rear+1==self.size:
            self.rear=0
        else:
            self.rear+=1
            #self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=item
        print(f"Element enqueue:{item}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            if self.front+1==self.size:
                self.front=0
            else:
                self.front+=1
        print(f"Dequeue:{items}")
    def peek():
        if is_empty():
            print("queue is empty")
            return None
        return self.queue[self.front]
    def display():
        if is_empty():
            print("queue is empty")
            return None
        if self.rear>=self.front:
            print("Queue:",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        else:
            print("Queue:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
