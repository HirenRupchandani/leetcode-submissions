class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already = 0
        best_satisfied = 0
        current = 0
        for i, customer in enumerate(customers):
            
            
            # Satisfied
            if grumpy[i] == 0:
                already += customer
            else :
                current += customer
            if i >= minutes:
                current -= customers[i - minutes] * grumpy[i - minutes]
                
            best_satisfied = max(best_satisfied, current)
        
        
        # for i, customer in enumerate(customers):
        #     current += customer
        #     if i >= minutes:
        #         current -= customers[i-minutes]
        #     best_satisfied = max(best_satisfied, current)
            
        return already + best_satisfied
