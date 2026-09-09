class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count={0: 1}
        perfix_sum=0
        answer=0
        for num in nums:
            perfix_sum+=num
            remainder=perfix_sum%k
            if remainder in count:
                answer+=count[remainder]
            count[remainder]=count.get(remainder, 0)+1
        return answer
