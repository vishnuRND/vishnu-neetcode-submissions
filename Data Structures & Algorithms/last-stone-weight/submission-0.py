class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones_heap = list()
        for stone in stones:
            heapq.heappush(stones_heap, -stone)

        while stones_heap and len(stones_heap) > 1:
            stone1 = -heapq.heappop(stones_heap)
            stone2 = -heapq.heappop(stones_heap)
            if stone1== stone2:
                continue
            else:
                heapq.heappush(stones_heap,-abs(stone1-stone2))
        
        if not stones_heap:
            return 0
        else:
            return -stones_heap[0]
        


        