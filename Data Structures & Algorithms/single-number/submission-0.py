class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        results = 0
        for i in range(len(nums)):
            results ^= nums[i]

        return results