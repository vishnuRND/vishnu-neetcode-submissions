class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            char_ord = ord(char)-ord('a')
            if node.children[char_ord] == None:
                node.children[char_ord] = TrieNode()
            node = node.children[char_ord]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.recur_search(self.root, word, 0)

    def recur_search(self, node, word, index):
        if index == len(word):
                if not node:
                    return False
                else:
                    return node.isEndOfWord
        if word[index] != ".":
            char_ord = ord(word[index])-ord('a')
            if node.children[char_ord] == None:
               return False
            return self.recur_search(node.children[char_ord], word, index+1)
        else:
            wordPresent = False
            for child in node.children:
                if child!=None:
                    wordPresent = wordPresent or self.recur_search(child, word, index+1)
            return wordPresent


        
