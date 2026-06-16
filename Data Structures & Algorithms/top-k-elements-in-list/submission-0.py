class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        lst=[]
        freq=[[] for _ in range(len(nums)+1)]
        for i in nums:
            count[i]=count.get(i,0)+1
        for key,value in count.items():
            freq[value].append(key)
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]: 
                lst.append(j)
        return lst[:k]

