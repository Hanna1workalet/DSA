class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horiCount = 0
        vertiCaunt = 0
        for i in moves:
            if i == "U":
                horiCount += 1
            elif i == "D":
                horiCount -= 1
            elif i == "L":
                vertiCaunt += 1
            else:
                vertiCaunt -= 1
        return horiCount == 0 and vertiCaunt == 0