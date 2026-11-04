class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[1] > nums[0]:
            for i in range(1,len(nums)-1):
                if nums[i+ 1] >= nums[i]:
                    continue
                elif nums[i+1] < nums[i]:
                    return False
            return True
        elif nums[1] < nums[0]:
            for i in range(1,len(nums)-1):
                if nums[i+ 1] <= nums[i]:
                    continue
                elif nums[i+1] > nums[i]:
                    return False
            return True
        else:
            return isMonotonic(nums[1::])