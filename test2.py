class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
            print(current.children)

    def find(self, word):
        '''
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        '''
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

x=['noha','ahmed']
node = PrefixTree()
for i in x :
    node.insert(i)
print(node.find('no').text)