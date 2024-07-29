class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        n = len(rating)
        
        for j in range(1, n-1):
            lLess = lGreat = rLess = rGreat = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    lLess += 1
                elif rating[i] > rating[j]:
                    lGreat += 1

            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    rLess += 1
                elif rating[k] > rating[j]:
                    rGreat += 1
            
            result += lLess * rGreat + lGreat * rLess

        return result
        