class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n=len(s)
        answer=[0]*n
        distance=n
        for i in range(n):
            if s[i]==c:
                distance=0
            else:
                distance+=1
            answer[i]=distance
        distance=n
        for i in range(n-1,-1,-1):
            if s[i]==c:
                distance=0
            else:
                distance+=1
            answer[i]=min(answer[i],distance)
        return answer
        
        