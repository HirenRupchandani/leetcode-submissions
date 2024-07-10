class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = []
        current_time_cooking = 0
        for arrival, prep_time in customers:
            # If idle -> current_time_cooking is smaller than arrival
            if current_time_cooking < arrival:
                # Start immediately and add the end time
                current_time_cooking = prep_time + arrival
            # If not idle, add the prep time to current_time_cooking
            else:
                current_time_cooking += prep_time
            # Remove the arrival time for that interval from current_time_cooking
            # And add to waiting time list
            waiting.append(current_time_cooking - arrival)
        return sum(waiting) / len(customers)