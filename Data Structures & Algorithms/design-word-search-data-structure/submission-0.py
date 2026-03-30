class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, i):

            if i >= len(word):
                return node.is_end
            
            if word[i] == ".":
                orginal_node = node
                i += 1
                for child in node.children:
                    node = orginal_node.children[child]
                    if dfs(node, i) == True:
                        return True
                return False
            
            elif word[i] in node.children:
                node = node.children[word[i]]
                i += 1
                return dfs(node, i)
            
            return False
        
        return dfs(node, 0)


            
        
