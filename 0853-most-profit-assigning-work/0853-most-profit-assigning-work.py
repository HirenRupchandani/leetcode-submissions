class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        n = len(jobs)
        total = 0
        best = 0
        i = 0
        for person in worker:
            # Increase the best profit up to the current worker's ability
            # worker with capacity 4,5 can finish job with difficulty 4. So max profit will be same for both.
            while i < n and jobs[i][0] <= person:
                best = max(best, jobs[i][1])
                i += 1
             # Add the best profit the current worker can get
            total += best

        return total
            
