class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = nums[0]
        cur = 0
        for n in nums:
            cur += n
            if cur > max:
                max = cur
            if cur < 0:
                cur = 0
        return max