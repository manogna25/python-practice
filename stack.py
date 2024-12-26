#stack
#basic way
'''l=[]
l.append(10)
l.append(34)
l.append(4)
l.append(349)
l.append(67)
l.append(90)
print(l)
a=l.pop()
print(a)
is_empty=len(l)==0
print(is_empty)
size=len(l)
print(size)
'''
#intermideate way
'''class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.isempty():
            print("List is empty")
        return self.items.pop()
    def isempty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def display(self):
        if self.isempty():
            print("stack is empty")
        else:
            for i in self.items:
                print(i,end=" ")
            print()
    def remove(self,element):
        if self.isempty():
            print("stack is empty")
        else:
            return self.items.remove(element)
m=Stack()
m.push(899)
m.push(435)
m.push(23)
m.push(63)
m.push(26)
m.push(12)
m.display()
m.pop()
m.pop()
m.display()
m.remove(23)
m.display()
'''
'''def push():
    n=int(input("enter the value to bo inserted:"))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
        print(n,"is inserted into stack")
def pop():
    if len(stack)==0:
        print("Not possible")
    else:
        print(stack[0],"is deleted from the stack")
        del stack[0]
def display():
     if len(stack)==0:
         print("stack is empty")
     else:
         print("elements of stack")
         for i in stack:
            print(i,end=" ")
         print("\nelement at top:",stack[0])

stack=list()
while(1):
    print("Enter the option below \n 1-Push \n 2-pop \n 3-display \n enter any key")
    str=input()
    if str=='1':
        print("PUSH")
        push()
    elif str=='2':
        print("POP")
        pop()
    elif str=='3':
        print("DISPLAY")
        display()
    else:
        print("option not available")
        break
'''
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        data=int(input("enter the value to be inserted:"))
        newnode=Node(data)
        if self.top is None:
            self.top=newnode
            self.top.next=None
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped element is :",self.top.data)
            print("----------")
            self.top=None
        else:
            temp=self.top
            print("Popped element is :",self.top.data)
            print("----------")
            self.top=temp.next
            temp=None
    def display(self):
        if self.top is None:
            print("Stack is empty")
            print("----------")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of stack is:",self.top.data)
m=Stack()
while(1):
    print("Enter the option below \n 1-Push \n 2-pop \n 3-display \n4-Exit enter any key")
    op=int(input())
    if op==1:
        print("PUSH")
        m.push()
    elif op==2:
        print("POP")
        m.pop()
        print("----------")
    elif op==3:
        print("DISPLAY")
        print("----------")
        m.display()
        print("----------")
    else:
        print("Exit")
        break
m.push()
m.push()
m.push()
m.push()
m.push()
m.display()
m.pop()
m.display()'''
#fixed size
'''class fixedsizestack:
    def __init__(self,max_size):
        self.stack=[0]* max_size
        self.top=-1
        self.max_size=max_size
    def is_full(self):
        return self.top==self.max_size-1
    def is_empty(self):
        return self.top==-1
    def push(self,data):
        if self.is_full():
            print("stack is full. cannot push data.")
        else:
            self.top+=1
            self.stack[self.top]=data
            print(f"pushes {data} into the stack")
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        else:
            data=self.stack[self.top]
            self.top-=1
            print(f"poped {data} from the stack")
            return data
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        else:
            print("Top of stack is:",self.stack[self.top])
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            print("----------")
        else:
            print(self.stack[:self.top+1])
m=fixedsizestack(9)
m.push(43)
m.push(3453)
m.push(4)
m.push(9)
m.display()
m.pop()
m.display()
m.push(435)
m.push(23)
m.push(63)
m.push(26)
m.push(12)
m.display()
m.push(7)
'''
#two stack fixed size:
class Twostackfixedsize:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.mid=(n+1)//2
        self.top1=-1
        self.top2=self.mid-1
    def push1(self,data):
        if self.top1<self.mid-1:
            self.top1+=1
            self.arr[self.top1]=data
            print(f"pushes {data} into the stack")
        else:
            print("stack is overflow")
    def push2(self,data):
        if self.top2<self.size-1:
            self.top2+=1
            self.arr[self.top2]=data
            print(f"pushes {data} into the stack")
        else:
            print("stack is overflow")
    def pop1(self):
        if self.top1>=0:
            data=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            print(f"poped {data} from the stack")
            return data
        else:
            print("stack is underflow")
            return None
    def pop2(self):
        if self.top2>=self.size:
            data=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2-=1
            print(f"poped {data} from the stack")
            return data
        else:
            print("stack is underflow")
            return None
    def display(self):
        print(f"Array:{self.arr}")
        print(f"stack1:{self.arr[self.mid:]}")
        print(f"stack2:{self.arr[self.mid:]}")
m=Twostackfixedsize(10)
while(1):
    print("Enter the option below \n 1-Push \n 2-pop \n 3-display \n4-Exit enter any key")
    op=int(input())
    if op==1:
        print("PUSH")
        m.push()
    elif op==2:
        print("POP")
        m.pop()
        print("----------")
    elif op==3:
        print("DISPLAY")
        print("----------")
        m.display()
        print("----------")
    else:
        print("Exit")
        break
m.push1(43)
m.push1(3453)
m.push2(4)
m.push2(9)
m.display()
    
       
