class TrieNode:
    # Dict of type <Character, TrieNode>
    children = None
    is_word = False

    def __init__(self):
        self.children = dict()


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]

        root.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for i in word:
            if i not in root.children:
                return False
            root = root.children[i]
        
        if root.is_word:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for i in prefix:
            if i not in root.children:
                return False
            root = root.children[i]

        return True


# trie = Trie()
# trie.insert("apple")
# print("--apple---", trie.search("apple"))   # returns true
# print("----app---", trie.search("app"))     # returns false
# print("----app---", trie.startsWith("app"))  # returns true
# trie.insert("app")
# print("----app---", trie.search("app"))     # returns true


# tree = trie.root
# while len(tree.children) > 0:
#     x = list(tree.children.keys())
#     print(x[0])
#     tree = tree.children[x[0]]

class StreamChecker:
    
    def __init__(self, words):
        self.queries = []
        self.combination = []
        self.trie = Trie()
        for i in words:
            self.trie.insert(i)
        
    def update_comb(self, letter):
        for i in range(len(self.combination)):
            self.combination[i] += letter
        
        self.combination.append(letter)

    def query(self, letter: str):
        self.queries.append(letter)
        if self.trie.search(letter):
            return True
        
        self.update_comb(letter)
        
        for i in self.combination:
            if self.trie.search(i):
                return True
        
        return False


obj = StreamChecker(["cd","f","kl"])
print(obj.query('a'))
print(obj.query('b'))
print(obj.query('c'))
print(obj.query('d'))
print(obj.query('e'))
print(obj.query('f'))
print(obj.query('g'))
print(obj.query('h'))
print(obj.query('i'))
print(obj.query('j'))
print(obj.query('k'))
print(obj.query('l'))