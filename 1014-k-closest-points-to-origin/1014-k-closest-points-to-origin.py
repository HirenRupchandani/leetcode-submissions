class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heapDist = []
        for x,y in points:
            distance = (x**2 + y**2)**(1/2)
            heapq.heappush(heapDist, (distance, x, y))
        while k!=0 and heapDist:
            distance, x, y = heapq.heappop(heapDist)
            result.append((x, y))
            k-=1
        return result



        