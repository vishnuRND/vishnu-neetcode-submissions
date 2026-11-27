class DLL:
        def __init__(self, key=0,val=0):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_metadata = dict()
        self.head = DLL()
        self.tail = DLL()
        self.head.right = self.tail
        self.tail.left = self.head
        

    def _remove(self, node):
            node.left.right, node.right.left = node.right, node.left

    def _append(self,node):

       node.left, node.right = self.tail.left, self.tail
       self.tail.left.right = node
       self.tail.left= node

    def get(self, key: int) -> int:
        node = self.node_metadata.get(key)
        if not node:
            return -1
        self._remove(node)
        self._append(node)
        return node.val
    

    def put(self, key: int, value: int) -> None:
        node = self.node_metadata.get(key)
        if node:
            node.val = value
            self._remove(node)
        else:
            if len(self.node_metadata) == self.capacity:
                lru = self.head.right
                self.head = self.head.right
                del self.node_metadata[lru.key]
            node = DLL(key, value)
            self.node_metadata[key] = node
        self._append(node)



        
