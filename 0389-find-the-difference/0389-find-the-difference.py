class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sortedS = sorted(s)
        sortedT = sorted(t)
        for i in range(len(t)):
            if i >= len(s):
                return sortedT[i]
            elif sortedS[i] != sortedT[i]:
                return sortedT[i]