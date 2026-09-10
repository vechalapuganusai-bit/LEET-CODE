class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index={0: -1}
        perfix_sum=0
        for i in range(len(nums)):
            perfix_sum+=nums[i]
            remainder=perfix_sum%k
            if remainder in remainder_index:
                if i-remainder_index[remainder]>=2:
                    return True
            else:
                remainder_index[remainder]=i
        return False
        