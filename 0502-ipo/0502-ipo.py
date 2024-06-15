class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Sort a combination of (capital, profit) on the basis of profit
        projects = [(capital[i], profits[i]) for i in range(len(capital))]
        projects.sort()

        # Use a maxHeap
        maxHeap = []
        for _ in range(k):
            # If a project capital is affordable, push the profit to heap
            while projects and projects[0][0] <= w:
                cap, prof = projects.pop(0)
                heapq.heappush(maxHeap, -prof)

            # If heap is empty, we can't afford any projects, so return the current capital         
            if not maxHeap:
                break
            
            # Calculate the overall capital
            w -= heapq.heappop(maxHeap)

        # Return final capital
        return w


        # heap = {}
        # for i in range(len(capital)):
        #     heap[capital[i]] = heap.get(capital[i], []) + [profits[i]]
        # heap = [(cap, sorted(prof, reverse=True)) for cap, prof in heap.items()]
        # heapq.heapify(heap)
        # while k and heap:
        #     cap, profs = heapq.heappop(heap)
        #     prof = profs.pop(0)
        #     # print(cap, prof)
        #     if profs:
        #         heapq.heappush(heap, (cap, profs))
        #     k-=1
        #     if cap > w:
        #         return w
        #     else:
        #         w += prof
        # return w


