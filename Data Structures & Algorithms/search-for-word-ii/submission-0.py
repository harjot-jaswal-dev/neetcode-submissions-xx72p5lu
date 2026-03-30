class TrieNode:

    def __init__(self):

        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        node = root
        rows = len(board)
        cols = len(board[0])
        output = set()
        
        for word in words:
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node = root
        # added all words in trie

        def nagivate(row, col, node, curr_word):

            if row >= rows or col >= cols or row < 0 or col < 0:
                return
            
            curr_letter = board[row][col]
            moves = ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1))

            if curr_letter in node.children:
                curr_word += board[row][col]
                orginal_word = board[row][col]
                orginal_node = node # current node
                board[row][col] = "#" # marked
                node = node.children[curr_letter] # moved node
                if node.is_end == True:
                    output.add(curr_word) # need to build and append the current_word if valid
                for move in moves: # all possible moves
                    r, c = move
                    if 0 <= r < rows and 0 <= c < cols:
                        nagivate(r, c, node, curr_word)
                board[row][col] = orginal_word # reassign if not matching, 

        for row in range(rows):
            for col in range(cols):
                nagivate(row, col, node, "")

        return list(output)

