class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curMax = nums[0]
        gmax = curMax
        curMin = nums[0]
        gmin = curMin
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            if curMax < 0:
                curMax = nums[i]
            else:
                curMax += nums[i]
            if curMax > gmax:
                gmax = curMax 
            if curMin > 0:
                curMin = nums[i]
            else:
                curMin += nums[i]
            if curMin < gmin:
                gmin = curMin
        print(gmin)
        return max(gmax, total - gmin) if gmax > 0 else gmax