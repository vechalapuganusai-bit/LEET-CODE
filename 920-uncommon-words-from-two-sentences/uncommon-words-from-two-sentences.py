class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        count={}
        for word in s1.split():
            count[word]=count.get(word,0)+1
        for word in s2.split():
            count[word]=count.get(word,0)+1
        result=[]
        for word in count:
            if count[word]==1:
                result.append(word)
        return result
        