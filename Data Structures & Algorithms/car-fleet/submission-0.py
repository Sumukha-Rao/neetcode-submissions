class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        maxtime=0
        fleet=0
        for pos,spd in cars:
            time=(target-pos)/spd
            if time>maxtime:
                fleet+=1
                maxtime=time
        return fleet
