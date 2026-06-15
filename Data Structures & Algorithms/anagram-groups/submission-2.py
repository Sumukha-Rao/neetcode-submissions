class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in range(len(strs)):
            count=[0]*26
            for j in strs[i]:
                count[ord(j)-ord('a')]+=1
            count=tuple(count)
            if count in group:
                group[count].append(strs[i])
            else:
                group[count]=[strs[i]]
        output=[]
        for i in group:
            output.append(group[i])
        return output

