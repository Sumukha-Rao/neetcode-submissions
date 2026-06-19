class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longsub=set()
        maxlen=0
        for i in range(len(s)):
            while s[i] in longsub:
                longsub.remove(s[i-len(longsub)])                
            longsub.add(s[i])
            maxlen=max(len(longsub),maxlen)
        return maxlen

        