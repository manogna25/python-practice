#Trees
class Node:
    def __init__(self,data):
        self.value=data
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insertrecur(self.root,data)
    def insertrecur(self,current,data):
        if current.left is None:
            current.left=Node(data)
        elif current.right is None:
            current.right=Node(data)
        else:
            self.insertrecur(current.left,data)
    def inorder_traversal(self):
        return self.inorder_traversal_recur(self.root)
    def inorder_traversal_recur(self,current):
        if current is None:
            return []
        return (self.inorder_traversal_recur(current.left)+[current.value]+(self.inorder_traversal_recur(current.right)))
    def preorder_traversal(self):
        return self.preorder_traversal_recur(self.root)
    def preorder_traversal_recur(self,current):
        if current is None:
            return []
        return ([current.value]+self.preorder_traversal_recur(current.left)+(self.preorder_traversal_recur(current.right)))
    def postorder_traversal(self):
        return self.postorder_traversal_recur(self.root)
    def postorder_traversal_recur(self,current):
        if current is None:
            return []
        return (self.postorder_traversal_recur(current.left)+(self.postorder_traversal_recur(current.right))+[current.value])    
    
m=BinaryTree()
m.insert(23)
m.insert(212)
m.insert(4)
m.insert(1)
m.insert(2321)
m.insert(5)
print(m.inorder_traversal())
print(m.postorder_traversal())
print(m.preorder_traversal())
