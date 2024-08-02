## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_end_of_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        pass

    def insert(self, word):
        ## Add a word to the Trie
        pass

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        pass
