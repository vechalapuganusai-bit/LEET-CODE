class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen={}
        for i in range(len(nums)):
            if nums[i] in last_seen:
                previous_index=last_seen[nums[i]]
                if i-previous_index<=k:
                    return True
            last_seen[nums[i]]=i
        return False

