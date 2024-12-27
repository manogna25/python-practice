class BSTNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key
    
class BST:
    def __init__(self):
        self.root=None
    def insert(self,key):
        if self.root is None:
            self.root=BSTNode(key)
        else:
            self.insert_recur(self.root,key)
    def insert_recur(self,current,key):
        if key<current.value:
            if current.left is None:
                current.left=BSTNode(key)
            else:
                self.insert_recur(current.left,key)
        else:
            if current.right is None:
                current.right=BSTNode(key)
            else:
                self.insert_recur(current.right,key)
    def search(self,key):
        return self.search_recur(self.root,key)
    def search_recur(self,current,key):
        if current is None or current.value==key:
            return current
        if key<current.value:
            return self.search_recur(current.left,key)
        return self.search_recur(current.right,key)
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
m=BST()
m.insert(23)
m.insert(43)
m.insert(3)
m.insert(21)
m.insert(34)
m.insert(1)
m.insert(66)
searchkey=int(input("enter element to search:"))
a=m.search(searchkey)
if a:
    print(f"Node with {searchkey} is found")
else:
    print("not found")
print(m.inorder_traversal())      
print(m.preorder_traversal())
print(m.postorder_traversal())
