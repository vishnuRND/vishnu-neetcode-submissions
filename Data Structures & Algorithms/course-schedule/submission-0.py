class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        inorder = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            inorder[a]+=1
        
        queue = deque()
        for i in range(numCourses):
            if inorder[i] == 0:
                queue.append(i)

        while queue:
            len_q = len(queue)
            numCourses -= len_q
            for _ in range (len_q):
                pop_ele = queue.popleft()
                for child in graph[pop_ele]:
                    inorder[child] -=1
                    if inorder[child] == 0:
                        queue.append(child)

        return True if numCourses == 0 else False
