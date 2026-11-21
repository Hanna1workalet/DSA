class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or  len(s)%2!=0:
            return False

        myDict = {")": "(", "}" : "{", "]" : "["}
        myStack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                myStack.append(i)
            elif not myStack:
                return False
            elif (i == ")" or i == "]" or i == "}"):
                if myStack[-1] == myDict[i]:
                    myStack.pop()
                else:
                    return False
        return not myStack

