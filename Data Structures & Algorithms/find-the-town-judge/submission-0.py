class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score=[0]*(n+1)
        for p1,p2 in trust:
            score[p1]-=1
            score[p2]+=1
        for person in range(1,n+1):
            if score[person]==n-1:
                return person
        return -1

            
