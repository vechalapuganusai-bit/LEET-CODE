class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary=bin(n)[2:]
        result=""
        for bit in binary:
            if bit=='0':
                result+='1'
            else:
                result+='0'
        return int(result,2)
        