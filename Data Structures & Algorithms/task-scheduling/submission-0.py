class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        freq=Counter(tasks)
        max_freq=max(freq.values())
        max_count=sum(1 for x in freq.values() if x==max_freq)
        return max(len(tasks),(max_freq-1)*(n+1)+max_count)