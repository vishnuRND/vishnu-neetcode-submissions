class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        result = [float('inf')] * (n+1)
        queue = list()
        queue.append([0,k])
        result[k] = 0
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append([v,t])
        while queue:
            distance, node = heapq.heappop(queue)
            if distance > result[node]:
                continue
            
            for children in graph[node]:
                v, dist = children
                if dist + distance < result[v]:
                    result[v] = dist + distance
                    heapq.heappush(queue, [result[v], v])
        minTime = float("-inf")
        for i in range(1, n+1):
            if result[i] == float('inf'):
                return -1
            minTime = max(result[i],minTime)
    
        return minTime
            
        