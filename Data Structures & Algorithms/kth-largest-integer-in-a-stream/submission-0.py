class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify_max(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums, val)
        return heapq.nlargest(self.k,self.nums)[-1]