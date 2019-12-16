class TrieNode:
    def __init__(self):
        self.childrens = dict()
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.childrens:
                node.childrens[ch] = TrieNode()
            node = node.childrens[ch]
            node.words.append(word)
            node.words.sort()
            
    def search(self,word):
        res = []
        node = self.root
        for ch in word:
            if ch not in node.childrens:
                break
            node = node.childrens[ch]
            res.append(node.words[:3])
        for rem in range(len(word) - len(res)):
            res.append([])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            trie.insert(prod)
        return trie.search(searchWord)
