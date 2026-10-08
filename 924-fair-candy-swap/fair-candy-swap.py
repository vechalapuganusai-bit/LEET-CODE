class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice_total=sum(aliceSizes)
        bob_total=sum(bobSizes)
        different=(alice_total-bob_total)//2
        bob_set=set(bobSizes)
        for x in aliceSizes:
            y=x-different
            if y in bob_set:
                return [x,y]        