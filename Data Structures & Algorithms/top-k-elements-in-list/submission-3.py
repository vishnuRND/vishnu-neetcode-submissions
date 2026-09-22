class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = list()
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        curr_element = 0
        for key in count:
            if curr_element == k:
                if count[key] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [count[key], key])
            else:
                heapq.heappush(heap, [count[key], key])
                curr_element += 1
    
        result = list()
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        