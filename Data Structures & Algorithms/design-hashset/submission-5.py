class MyHashSet:

    def __init__(self):
        self.seen = defaultdict(int)

    def add(self, key: int) -> None:
        self.seen[key] = 1

    def remove(self, key: int) -> None:
        if key in self.seen:
            del self.seen[key]

    def contains(self, key: int) -> bool:
        return key in self.seen        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)