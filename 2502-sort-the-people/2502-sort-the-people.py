class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        heap = [(heights[i], names[i]) for i in range(n)]
        heap = sorted(heap, reverse=True)
        return [heap[i][1] for i in range(n)]
