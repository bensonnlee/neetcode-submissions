class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_bank = set()
        for word in wordList:
            word_bank.add(word)

        if endWord not in word_bank:
            return 0

        q = deque([beginWord])
        word_bank.discard(beginWord)

        length = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return length

                for i in range(len(word)):
                    for c in range(ord('a'), ord('z') + 1):
                        candidate = word[:i] + chr(c) + word[i+1:]
                        if candidate in word_bank:
                            q.append(candidate)
                            word_bank.discard(candidate)
            
            length += 1

        return 0
