class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            result = target - i
            if result in nums[nums.index(i)+1:]:
                    return [nums.index(i), nums.index(result, nums.index(i)+ 1)]
        