class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

class Solution:
    def countOfPeaks(self, nums, queries):
        n = len(nums)
        peaks = set()
        fenwick_tree = FenwickTree(n)

        def is_peak(i):
            if i <= 0 or i >= n - 1:
                return False
            return nums[i - 1] < nums[i] > nums[i + 1]

        def update_peak(i):
            if i <= 0 or i >= n - 1:
                return
            if is_peak(i):
                if i not in peaks:
                    peaks.add(i)
                    fenwick_tree.update(i + 1, 1)
            else:
                if i in peaks:
                    peaks.remove(i)
                    fenwick_tree.update(i + 1, -1)

        # Initialize the peaks set and Fenwick Tree
        for i in range(1, n - 1):
            if is_peak(i):
                peaks.add(i)
                fenwick_tree.update(i + 1, 1)

        results = []

        for query in queries:
            if query[0] == 2:
                _, index, value = query
                nums[index] = value
                for i in range(max(1, index - 1), min(n - 1, index + 2)):
                    update_peak(i)
            elif query[0] == 1:
                _, li, ri = query
                if li == ri or li + 1 == ri:
                    results.append(0)
                else:
                    results.append(fenwick_tree.range_query(li + 2, ri))

        return results