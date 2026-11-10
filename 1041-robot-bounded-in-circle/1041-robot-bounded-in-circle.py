class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = ["north", "west", "south", "east"] 
        dir = "north"
        vector = [0,0]
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
            elif i == "R":
                dir = dirs[(dirs.index(dir) - 1) % 4]
        if vector == [0,0]:
            return True
        elif dir != "north":
            return True
        else: 
            return False