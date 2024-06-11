class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hmap = {}
        common = []
        uncommon = []
        for num in arr1:
            hmap[num] = hmap.get(num,0) + 1
        print('hmap:', hmap)
        for num in arr2:
            common += [num]*hmap[num]
            del hmap[num]

        for num in sorted(hmap):
            common+= [num] * hmap[num] 

        print(common)
        return common