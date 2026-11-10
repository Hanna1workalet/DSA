class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = ["north", "west", "south", "east"] 
        dir = "north"
        deg = 0
        vector = [0,0]
        dirchange = 0
        for i in instructions:
            if i == "G":
                if dir == "north":
                    vector[1] += 1
                elif dir == "west":
                    vector[0] -= 1
                elif dir == "south":
                    vector[1] -= 1
                elif dir == "east":
                    vector[0] += 1
            elif i == "L":
                dir = dirs[(dirs.index(dir) + 1) % 4] 
                deg -= 90
                dirchange += 1
            elif i == "R":
                dir = dirs[(dirs.index(dir) - 1) % 4]
                deg += 90
                dirchange += 1
        if vector == [0,0]:
            return True
        elif abs(deg) != 0 and abs(deg) % 360 != 0:
            return True
        else: 
            return False