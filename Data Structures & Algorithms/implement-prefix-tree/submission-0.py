class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfword = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            i = ord(char)-ord('a')
            if node.children[i] == None:
                 node.children[i] = TrieNode()
            node = node.children[i]
        node.endOfword = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            i = ord(char)-ord('a')
            if node.children[i] == None:
                 return False
            node = node.children[i]
        return node.endOfword
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            i = ord(char)-ord('a')
            if node.children[i] == None:
                 return False
            node = node.children[i]
        return True
        
        