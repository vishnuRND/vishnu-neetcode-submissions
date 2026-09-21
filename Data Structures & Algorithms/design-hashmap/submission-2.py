class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if not node:
            return -1
        if node.key == key:
            return node.val
        if node.key < key:
            return self.search(node.right, key)
        if node.key > key:
            return self.search(node.left, key)
    
    def insert(self,node, key,val):
        if not node:
            return TreeNode(key,val)
        if node.key == key:
            node.val = val
        if node.key < key:
            node.right = self.insert(node.right, key,val)
        if node.key > key:
            node.left = self.insert(node.left, key,val)
        return node

    def delete(self,node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            next = node.right
            while next.left:
                next = next.left
            node.key = next.key
            node.val = next.val
            node.right = self.delete(node.right, next.key)
        return node

    def add(self,key,val):
        self.root = self.insert(self.root, key,val)
    
    def remove(self,key):
        self.root = self.delete(self.root, key)
        
    def find(self,key):
        return self.search(self.root, key)
class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [BST() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        self.buckets[idx].add(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        return self.buckets[idx].find(key)
        

    def remove(self, key: int) -> None:
        idx = key % self.size
        self.buckets[idx].remove(key)


# obj.remove(key)