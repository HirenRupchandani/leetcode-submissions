import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # most instinct method
        max_length = 1
        left = 0 # We want to have a sliding window so that we can know the length of the window (i.e. the possible solution, thus we named the start of the window "left")
        min_heap = [] # named min_heap because this heap's purpose is to find the minimum
        max_heap = [] # named max_heap because this heap's purpose is to find the maximum
        for right in range(len(nums)): # "right" is the right end of the window
            # first of all, we push the [right] element to both the min_heap and the max_heap
            # because we need to first "slide" the window 
            # we also need the index information because we need to make sure our min and max is valid while we are sliding the window
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            # in this step, we need to retrieve the minimum element and the maximum element in the window range, 
            # therefore, we need to make sure the maximum and the minimum are within window range (i.e. left <= index <= right)
            # thus we need to pop the minheap until we find the smallest element which is in the window
            # we also need to pop the maxheap until we find the largest element which is in the window
            while min_heap[0][1] < left:
                heapq.heappop(min_heap)
            while max_heap[0][1] < left:
                heapq.heappop(max_heap)

            # We find the minimum and the maximum in the window, we can check whether the window is valid or not
            if -max_heap[0][0] - min_heap[0][0] <= limit:
                # if it's valid, we can update the answer
                max_length = max(max_length, right - left + 1)
            else:
                # else we just move the left end of the window
                left += 1
        return max_length