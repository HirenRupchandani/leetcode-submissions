class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hmap = {}
        common = []
        arr1.sort()
        for num in arr1:
            hmap[num] = hmap.get(num,0) + 1
        for num in arr2:
            common += [num]*hmap[num]
            del hmap[num]

        for num in hmap:
            common+= [num] * hmap[num] 

        return common