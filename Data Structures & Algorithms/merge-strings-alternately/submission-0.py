class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        word=""
        minlength=min(len1,len2)
        for i in range(minlength):
            word+=word1[i]+word2[i]
        if len1<len2:
            word+=word2[minlength:]
        elif len2<len1:
            word+=word1[minlength:]
        return word
