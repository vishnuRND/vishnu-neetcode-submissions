class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if not node:
            return False
        if node.val == key:
            return True
        if node.val < key:
            return self.search(node.right, key)
        if node.val > key:
            return self.search(node.left, key)
    
    def insert(self,node, key):
        if not node:
            return TreeNode(key)
        if node.val < key:
            node.right = self.insert(node.right, key)
        if node.val > key:
            node.left = self.insert(node.left, key)
        return node

    def delete(self,node, key):
        if not node:
            return None
        if key < node.val:
            node.left = self.delete(node.left, key)
        elif key > node.val:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            next = node.right
            while next.left:
                next = next.left
            node.val = next.val
            node.right = self.delete(node.right, next.val)
        return node

    def add(self,key):
        self.root = self.insert(self.root, key)
    
    def remove(self,key):
        self.root = self.delete(self.root, key)
        
    def find(self,key):
        return self.search(self.root, key)
            
            
class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [BST() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not self.contains(key):
            self.buckets[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if self.contains(key):
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return bool(self.buckets[idx].find(key))

