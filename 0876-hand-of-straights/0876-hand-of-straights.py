class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        res = True
        if len(hand)%groupSize!=0:
            return False
        counter = {}
        for card in hand:
            counter[card] = counter.get(card, 0) + 1

        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first+groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i]==0:
                    if i!=minHeap[0]:
                        return False    # If there is a gap in the heap e.g., [1,2,3,1,4,3,5,6] -> 2 is just once so it won't form another group so false
                    heapq.heappop(minHeap)
        return True


            


