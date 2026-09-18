class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num]+=1
        topK = list()
        count = 0
        for frequency in frequencies:
            if count < k:
                heapq.heappush(topK,(frequencies[frequency],frequency))
                count+=1
            else:
                if topK[0][0] < frequencies[frequency]:
                       heapq.heappop(topK)
                       heapq.heappush(topK,(frequencies[frequency],frequency))
        result = list()
        for i in range(k):
            result.append((heapq.heappop(topK)[1]))
        return result       