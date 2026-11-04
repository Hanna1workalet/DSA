class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip(" ")
        for i in range(-1, -len(s) -1, -1):
            if s[i] != " ":
                count += 1
            else:
                return count 
        return count 
        