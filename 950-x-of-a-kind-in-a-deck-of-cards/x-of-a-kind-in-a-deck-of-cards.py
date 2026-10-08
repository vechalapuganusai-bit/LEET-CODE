from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        count={}
        for card in deck:
            count[card]=count.get(card,0)+1
        x=0
        for freq in count.values():
            x=gcd(x,freq)
        return x>=2

        