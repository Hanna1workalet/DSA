class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while count < len(nums):
            if nums[count] == 0 and not all(x == 0 for x in nums[count::]):
                nums.append(nums.pop(count))
            else:
                count +=1
        