class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClose = list()
        curr_count = 0
        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            if curr_count == k:
                if distance < -kClose[0][0]:
                    heapq.heappop(kClose)
                    heapq.heappush(kClose, [-distance, x, y])
            else:
                heapq.heappush(kClose, [-distance, x, y])
                curr_count+=1

        result = list()
        while kClose:
            distance, x, y = heapq.heappop(kClose)
            result.append([x, y])
        return result
        