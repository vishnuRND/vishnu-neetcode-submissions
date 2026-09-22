class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = list()
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        for key in count:
            heapq.heappush(heap, [-count[key], key])
        
        result = list()
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        