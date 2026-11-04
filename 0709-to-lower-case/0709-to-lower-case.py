class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in range(len(s)):
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                print(s[i])
                s = s.replace(s[i], chr(ord(s[i]) + 32))
                print(s[i])
        return s