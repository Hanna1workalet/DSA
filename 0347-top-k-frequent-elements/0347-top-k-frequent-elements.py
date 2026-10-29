class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(list)
        for i in set(nums):
            freq[nums.count(i)].append(i)
        res = []
        while len(res) < k:
            res.extend(freq.pop(max(freq.keys())))
        return res