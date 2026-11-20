class KthLargest:

    def insert(self, num):
        if self.curr_count == self.k:
            if num > self.kLargest[0]:
                heapq.heappushpop(self.kLargest, num)
        else:
            heapq.heappush(self.kLargest, num)
            self.curr_count +=1
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kLargest = list()
        self.curr_count = 0
        for num in nums:
            self.insert(num)

    def add(self, val: int) -> int:
        self.insert(val)
        return self.kLargest[0]

        
