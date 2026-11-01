class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(2, n+1):
            ss = s[:n//i:]
            if s.count(ss) == len(s) / len(ss):
                return True
        return False