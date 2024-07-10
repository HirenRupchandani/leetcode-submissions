class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = []
        current_time_cooking = 0
        for arrival, prep_time in customers:
            # If idle -> waiting time is smaller than arrival
            if current_time_cooking < arrival:
                # Start immediately and add the end time
                current_time_cooking = prep_time + arrival
            # If not idle, check the difference in current time and arrival
            else:
                current_time_cooking += prep_time
            waiting.append(current_time_cooking - arrival)
        return sum(waiting) / len(customers)
        
