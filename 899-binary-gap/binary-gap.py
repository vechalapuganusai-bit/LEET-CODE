class Solution:
    def binaryGap(self, n: int) -> int:
        binary=bin(n)[2:]
        max_distance=0
        last_one=-1
        for i in range(len(binary)):
            if binary[i]=='1':
                if last_one!=-1:
                    max_distance=max(max_distance,i-last_one)
                last_one=i
        return max_distance
        