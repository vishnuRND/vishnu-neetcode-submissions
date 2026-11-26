class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        result = list()

        graph = defaultdict(list)
        inorder = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            inorder[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inorder[i] == 0:
                queue.append(i)

        
        while queue:
                pop_ele = queue.popleft()
                numCourses -= 1
                result.append(pop_ele)
                for child in graph[pop_ele]:
                    inorder[child]-=1
                    if inorder[child] == 0:
                        queue.append(child)

        
        return result if numCourses ==0 else []

