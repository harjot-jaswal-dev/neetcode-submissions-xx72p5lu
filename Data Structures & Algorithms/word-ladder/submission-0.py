from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        if endWord not in wordList:
            return 0
        
        visited = set()
        wordList = set(wordList)
        level = 1
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)


        while queue:

            for i in range(len(queue)):
                
                curr_word = queue.popleft()

                if curr_word == endWord:
                    return level
                
                for word in wordList:

                    if word in visited:
                        continue
                    
                    difference = 0
                    for i in range(len(word)):

                        if word[i] != curr_word[i]:
                            difference += 1

                    if difference > 1:
                        continue
                
                    queue.append(word)
                    visited.add(word)

            level += 1
        
        return 0