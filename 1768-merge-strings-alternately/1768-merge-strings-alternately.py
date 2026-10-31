class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(max(len(word1),len(word2))):
            if len(word1) > i:
                merged += (word1[i])
            if len(word2) > i:
                 merged += (word2[i])
        return merged
