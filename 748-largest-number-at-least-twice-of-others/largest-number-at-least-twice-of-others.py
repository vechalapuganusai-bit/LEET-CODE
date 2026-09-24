class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        larget=max(nums)
        index=nums.index(larget)
        for num in nums:
            if num!=larget and larget<2*num:
                return -1
        return index
