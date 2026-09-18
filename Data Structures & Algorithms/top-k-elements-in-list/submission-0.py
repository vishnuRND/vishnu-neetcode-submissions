class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num]+=1
        topK = list()
        for frequency in frequencies:
            heapq.heappush(topK,(-1*frequencies[frequency],frequency))
        result = list()
        for i in range(k):
            result.append((heapq.heappop(topK)[1]))
        return result       