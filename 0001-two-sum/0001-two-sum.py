class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, n in enumerate(nums):
            if target-n in map:
                return [map[target-n], i]
            else:
                map[n] = i
        