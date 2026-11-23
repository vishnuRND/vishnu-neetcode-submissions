class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:    
        T = 0
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = deque()
        while heap or queue:
            T+=1
            if not heap:
                T = queue[0][1]
            else:
                cnt = 1+heapq.heappop(heap)
                if cnt:
                    queue.append([cnt,T+n])
            if queue and queue[0][1] == T:
                heapq.heappush(heap, queue.popleft()[0])
        return T