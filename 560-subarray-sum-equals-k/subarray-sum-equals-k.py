class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        perfix_sum=0
        answer=0
        count={0: 1}
        for num in nums:
            perfix_sum+=num
            if perfix_sum-k in count:
                answer+=count[perfix_sum-k]
            count[perfix_sum]=count.get(perfix_sum,0)+1
        return answer

        