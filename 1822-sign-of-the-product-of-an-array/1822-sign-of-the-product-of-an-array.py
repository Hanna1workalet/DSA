class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(x):
            if x >= 1:
                return 1
            elif x < 0:
                return -1
            elif x == 0:
                return 0
        product = 1
        for i in nums:
            product *= i
        return signFunc(product)