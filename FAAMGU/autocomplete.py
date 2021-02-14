# Design and implement auto complete feature. Assume the data is strings (could be anything - Example - All state names of India)

# Trie - N-array

# hit, hot, his, him

# root -> a, b, c, d, ..........


# Node() {
#     val
#     children = []
#     is_word = True
# }
import marisa_trie

PREFIX_LEN = 1
MIN_SIZE = 5
DATA_FILE = "data.txt"


class Autocomplete:
    def __init__(self):
        self.trie = None #marisa_trie.Trie(words)

    def read_data(self):
        words = set()
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            # print(lines)
            for line in lines:
                sentences = line.strip().split("\t")
                # print(line, len(line), line.split(" "))
                word_list = line.split(" ")

                for s in sentences:
                    words.add(s)
                for word in word_list:
                    words.add(word.strip())

        self.trie = marisa_trie.Trie(words)

    def get_keys(self, prefix, page=None):
        if len(prefix) >= PREFIX_LEN:
            if self.trie.has_keys_with_prefix(prefix):
                words = self.trie.keys(prefix)
                words = sorted(words)
                return words[:MIN_SIZE]
        
        return None
        
    


# words = ['foo', 'bar', 'foobar', 'fookey', 'foo1', 'foo2', 'key1', 'key2', 'key12']
auto = Autocomplete()
auto.read_data()
# print(auto.get_keys("Hell"))


# Let assume this is going to call from UI with different prefixes.
prefix = "foot"
for i in range(1, len(prefix)+1):
    print(prefix[:i], auto.get_keys(prefix[:i]))


