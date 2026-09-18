import random
class Solution:
    def quickSort(self,arr,low, high):
        if low < high:
            pivot = self.randomPartition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot+1, high)
        
    def randomPartition(self,arr, low, high):
        r_i = random.randint(low,high)
        arr[r_i], arr[high] = arr[high], arr[r_i]
        return self.partition(arr, low, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low,high):
            if arr[j] < pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
        
        