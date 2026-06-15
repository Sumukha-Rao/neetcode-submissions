class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in range(len(strs)):
            sstrs=str(sorted(strs[i]))
            if sstrs in group:
                group[sstrs].append(strs[i])
            else:
                group[sstrs]=[strs[i]]
        output=[]
        for i in group:
            output.append(group[i])
        return output

