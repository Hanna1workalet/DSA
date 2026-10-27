class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        while val in nums:
            nums.remove(val)
            k -= 1 
        