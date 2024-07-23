class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        hmap = {}
        h2 = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        print(hmap)
        for k,v in hmap.items():
            if v not in h2:
                h2[v] = []
            h2[v].append(k)
        print(h2)
        h2 = dict(sorted(h2.items()))
        print("sorted", h2)

        for k, v in h2.items():
            if len(v) > 1:
                v.sort(reverse=True)
                for i in range(len(v)):
                    result += [v[i]]*k
            else:
                result += [v[0]]*k
        print(result)
        return result