'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

class TrieNode:
   def __init__(self):
      self.children = {}
      self.end_of_word = False

        # to create a child with "a"
        #children["a"] = TrieNode()
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
              curr.children[c] = TrieNode()

            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  
print(trie.search("app"))    
trie.startsWith("app")
trie.insert("app")
print(trie.search("app"))    


'''
no idea what a trie is so watched the vid
Operation	    List Search	Trie Search
Insert "word"	O(1)	O(m)
Search "word"	O(n * m)	O(m)
Prefix Search   "wor"	O(n * m)	O(m)
'''