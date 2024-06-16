class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0
        hmap = {}
        for hour in hours:
            rem = hour%24
            complement = (24-rem)%24
            if complement in hmap:
                res += hmap[complement]
            if rem in hmap:
                hmap[rem] += 1
            else:
                hmap[rem] = 1
        return res