class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if len(arr) == 0 or len(arr) == 1:
            return len(arr)
        elif len(arr) == 2 and arr[0] != arr[1]:
            return 2
        if arr[0] != arr[1]:
            currLeng = 2
        else:
            currLeng = 1
        maxLeng = currLeng
        for i in range(1, len(arr)-1):
            if  (arr[i-1] < arr[i] or arr[i] < arr[i+1]) and (arr[i-1] > arr[i] or arr[i] > arr[i+1]):
                currLeng += 1
            else:
                if arr[i] != arr[i+1]:
                    currLeng = 2
                else:
                    currLeng = 1
            if currLeng > maxLeng:
                maxLeng = currLeng
        return maxLeng
            